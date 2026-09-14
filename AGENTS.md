# TRISHUL 2.0 — Codex Engineering Instructions

## Mission
Build TRISHUL 2.0 for SIH26192: an AI-assisted flash-flood risk, early-warning, evacuation-routing, and disaster-resilient reporting prototype for hilly regions.

This is a greenfield SIH prototype with two developers using separate Codex sessions. Build a reliable, demonstrable vertical slice first. Do not over-engineer.

## Source of truth
Read these before implementing substantial work:
1. `AGENTS.md` — engineering guardrails
2. `docs/CODEX_BUILD_PLAN.md` — execution sequence
3. `docs/TEAM_SPLIT.md` — ownership boundaries
4. `docs/codex-context/00_CODEX_START.md` — product master context
5. Relevant files in `docs/codex-context/` for the subsystem being changed

If the detailed context conflicts with the MVP guardrails here, prefer the simpler, testable implementation and document the decision.

## Team ownership
### Arunangshu Dasgupta — Platform / Backend / GIS
Owns `backend/`, `scripts/`, `data/`, backend tests, API/domain contracts, risk engine, routing, adapters, and integration infrastructure.

### Rutuj Runwal — Product / Frontend / Mobile
Owns `mobile/`, `dashboard/`, frontend/mobile tests, offline UX, maps, SOS/report UX, and demo presentation polish.

Do not edit the other teammate's owned area unless integration requires it. Coordinate API/schema changes through documentation and small commits.

## Non-negotiable engineering rules
1. Inspect the repository before changing anything.
2. Keep the application runnable after every major task.
3. Prefer simple deterministic implementations over speculative infrastructure.
4. Never claim scientific capabilities that are not implemented or validated.
5. Never hard-code secrets. Use environment variables and provide `.env.example`.
6. Never commit API keys, tokens, credentials, certificates, or private URLs.
7. Test core risk calculations, route safety/pruning, reports, and API contracts.
8. Use typed models at API boundaries.
9. Keep heavy GIS preprocessing offline/precomputed.
10. Demo Mode must work without internet.
11. Treat risk output as decision support, not a guaranteed prediction.
12. Avoid dependencies unless they solve a concrete MVP requirement.
13. Do not replace working code merely for style.
14. Before declaring a task complete, run relevant tests/static/build checks.
15. If a dependency cannot reliably run, use an adapter/interface and deterministic fallback rather than blocking the product.
16. Do not fabricate model accuracy, sensor measurements, training results, or emergency-service endorsements.

## Product truth
The prototype must demonstrate:
- rainfall-driven risk escalation
- terrain/elevation-aware risk visualization
- estimated hazard arrival vs evacuation time
- dynamic safe-route recalculation when roads become unsafe
- citizen SOS/blockage reports
- offline/demo operation
- administrative command dashboard

Optional integrations are not blockers:
- real BLE/Wi-Fi Direct
- native background barometer sensing
- bridge CCTV/YOLO
- acoustic TinyML
- live satellite processing
- live DEM preprocessing

## Scientific guardrails
Do not use atmospheric pressure drop as a primary flash-flood predictor; if shown, label it an auxiliary signal.
Do not claim universal 15-minute flood prediction. Use language such as `localized risk assessment` and `estimated hazard arrival`.
Do not imply simulated demo observations are live measured observations.

## Preferred architecture
```text
mobile/       Flutter citizen application
dashboard/    web command center
backend/      FastAPI modular monolith
data/         small deterministic demo fixtures
scripts/      preprocessing/data-generation utilities
tests/        cross-component tests
docs/         product and technical context
```

Backend separation:
- API routes
- Pydantic/domain models
- risk engine
- routing engine
- incident/report service
- demo scenario service
- external data adapters

Frontend separation:
- presentation
- state/application logic
- API client
- local persistence
- map/routing presentation
- emergency/report flows
- demo mode

## MVP priorities
P0:
1. FastAPI backend
2. deterministic transparent risk engine
3. deterministic scenario controls
4. safe route computation and pruning
5. Flutter citizen screens
6. command dashboard
7. Demo Mode
8. tests/documentation

P1:
- offline cache
- SQLite persistence
- report synchronization abstraction
- shelter management

P2:
- real BLE
- acoustic model
- YOLO bridge vision
- native barometer
- live external data ingestion
- large-scale GIS processing

## Risk engine baseline
Minimum inputs:
- rainfall intensity
- cumulative/upstream rainfall
- terrain/slope risk
- soil saturation/proxy
- observed water/torrent signal
- blockage/incident reports

Return:
- score `[0,1]`
- level `LOW/MODERATE/HIGH/EXTREME`
- confidence/data-quality metadata
- estimated hazard arrival minutes
- estimated evacuation minutes when route/user data exists
- recommended action

For the MVP, use a transparent configurable weighted model. XGBoost may be added as a real trained model only when training data and evaluation are legitimate; never use an untrained model as decoration.

## Routing baseline
Use a NetworkX-compatible graph. Edges should support distance/time, slope/elevation metadata where available, and closure/flood status. Unsafe edges are removed or strongly penalized. Route to high-ground shelters. Use small deterministic demo fixtures; do not require live OSM downloads during a demo.

## Demo Mode
Required scenarios:
- `NORMAL`
- `HEAVY_RAIN`
- `FLASH_FLOOD`
- `ROAD_BLOCKED`
- `CELLULAR_OUTAGE`

Reset must reproduce the same results every time.

## UI direction
Emergency-focused, modern, high contrast, clean typography, map-first. Avoid childish visuals and excessive gradients. Severity must not be communicated by color alone.

## Git discipline
- Work on feature branches.
- Make small coherent commits.
- Never rewrite history.
- Never delete teammate work.
- Keep default branch buildable.
- Coordinate changes to shared contracts.

## Completion protocol
1. Run backend tests.
2. Run mobile analyzer/tests/build checks available.
3. Run dashboard build/checks.
4. Verify Demo Mode.
5. Update documentation.
6. State exactly what works, what is simulated, and remaining limitations.
