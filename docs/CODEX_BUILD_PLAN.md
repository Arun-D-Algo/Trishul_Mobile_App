# TRISHUL 2.0 — Codex Build Plan

## How to use this file
This is the execution plan for two Codex sessions working on the same GitHub repository. `AGENTS.md` is the highest-priority repository engineering guidance. The files in `docs/codex-context/` are product/domain reference material. This file defines the practical MVP sequence.

Do not ask Codex to build the entire application in one pass. Execute one phase at a time, run verification, and commit.

## Non-negotiable MVP
The final demo must demonstrate one continuous path:

`scenario/weather inputs -> localized risk -> hazard/evacuation timing -> map impact -> safe route -> citizen warning -> incident/SOS -> dashboard`

Demo Mode must reproduce the same flow without internet.

## Architecture choice
Use a modular monolith for the backend and separate clients:

```text
Flutter mobile ───────┐
                      ├── FastAPI ── domain/risk/routing/demo/data adapters
Web dashboard ────────┘
                           │
                      SQLite/Postgres* 
```

`*` Start with SQLite or in-memory deterministic storage if PostgreSQL/PostGIS would slow development. Add PostGIS only when there is a concrete spatial query that needs it.

For maps, prefer MapLibre/flutter_map or another low-friction option over a paid/token-dependent provider. Do not make external map tiles a Demo Mode dependency.

## Phase 0 — Repository audit
Both agents:
- read `AGENTS.md`
- read `docs/CODEX_BUILD_PLAN.md`
- read relevant files in `docs/codex-context/`
- inspect all existing files before editing
- identify the current default branch and existing work

Do not overwrite another teammate's branch.

## Phase 1 — Arunangshu: backend foundation
Implement:
- Python project structure
- FastAPI app
- settings and `.env.example`
- Pydantic domain/API schemas
- `/api/v1/health`
- deterministic demo scenarios
- weather adapter interface + DemoWeatherProvider
- risk engine package
- tests

Acceptance:
- `GET /api/v1/health` works
- risk endpoint returns deterministic output
- all backend tests pass
- no secrets committed

## Phase 2 — Arunangshu: risk + routing
Implement:
- transparent weighted risk baseline
- configurable weights
- risk levels LOW/MODERATE/HIGH/EXTREME
- hazard arrival estimate
- evacuation-time comparison
- NetworkX graph abstraction
- shelter nodes
- road closure/flood status
- route pruning/reweighting
- `/api/v1/routes/evacuate`
- `/api/v1/reports`
- `/api/v1/roads/{edge_id}/status`
- `/api/v1/shelters`

Acceptance:
- heavy rain raises risk
- flash-flood scenario becomes EXTREME
- blocked bridge changes route
- tests cover route safety and risk thresholds

## Phase 3 — Rutuj: dashboard skeleton
While Arunangshu stabilizes API contracts, implement the dashboard against the documented schemas and deterministic local mock data if necessary.

Implement:
- responsive command-center layout
- map panel
- risk card
- rainfall/weather card
- alert list
- incident list
- shelter summary
- scenario selector
- rainfall control
- bridge/road block control

Do not duplicate risk/routing logic in frontend.

## Phase 4 — Rutuj: Flutter citizen app
Implement:
- home/risk screen
- risk severity indicator
- hazard arrival / evacuation timing
- map screen
- safe route presentation
- shelter information
- report hazard flow
- SOS flow
- network status indicator
- Demo Mode indicator

Use a typed API client. Keep API base URL configurable.

## Phase 5 — Rutuj: offline-first behavior
Implement local persistence for:
- cached risk snapshot
- shelters
- route/demo data
- pending reports/SOS

When offline:
- app continues to show cached critical data
- new reports enter a local queue
- UI clearly shows queued/sync-pending status

Implement a transport abstraction. A real BLE implementation is optional and must not block the MVP.

## Phase 6 — Integration
Arunangshu:
- connect real API to dashboard/mobile
- add CORS/configuration
- ensure response schemas remain backwards-compatible

Rutuj:
- replace mock data with API calls
- handle loading/error/offline states
- verify route and risk states render correctly

Both:
- run full tests
- verify normal -> heavy rain -> flash flood -> blocked road flow

## Phase 7 — optional sensor/AI adapters
Only after the end-to-end demo is stable.

Implement adapters, not mandatory dependencies:
- Open-Meteo live provider
- acoustic observation provider
- bridge vision observation provider
- barometer auxiliary signal
- satellite flood-evidence provider
- BLE/peer transport

If a real integration is unreliable, retain a deterministic fallback.

## Phase 8 — SIH polish
Implement:
- polished demo scenarios
- clear DEMO label
- error-safe fallbacks
- accessible warning presentation
- seed/reset demo button
- README setup instructions
- architecture diagram
- limitations and scientific-claim disclaimer

## Phase 9 — final verification
Backend:
- tests
- lint/type checks where configured
- API smoke test

Dashboard:
- build
- no console errors
- responsive layout

Mobile:
- analyzer
- tests where available
- Android build if environment permits

Demo:
- run with internet
- run without internet
- reset and reproduce the exact scenario

## Commit policy
Prefer commits such as:
- `feat(backend): add risk domain and demo scenarios`
- `feat(routing): add hazard-aware evacuation routing`
- `feat(dashboard): add command center shell`
- `feat(mobile): add citizen risk and evacuation screens`
- `feat(offline): add local emergency report queue`
- `test: add end-to-end demo scenario coverage`

Do not commit generated secrets, local databases, huge datasets, build artifacts, or API credentials.
