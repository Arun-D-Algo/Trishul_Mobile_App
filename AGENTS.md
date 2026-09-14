# TRISHUL 2.0 — Codex Engineering Instructions

## Mission
Build TRISHUL 2.0, an SIH prototype for problem statement SIH26192: an AI-assisted flash-flood risk, early-warning, offline evacuation-routing, and disaster-resilient reporting platform for hilly regions.

The repository is a greenfield monorepo. Build a demonstrable vertical slice first; do not over-engineer or chase production-grade hardware integrations during the 1-week prototype.

## Non-negotiable engineering rules
1. Inspect the repository before changing anything.
2. Keep the app runnable after every major task.
3. Prefer simple, deterministic implementations over speculative infrastructure.
4. Do not claim scientific capabilities that are not implemented or validated.
5. Never hard-code secrets. Use `.env` / platform environment variables and provide `.env.example`.
6. Never commit API keys, tokens, credentials, certificates, or private URLs.
7. Write tests for core risk calculations, route pruning, report validation, and API contracts.
8. Use typed models at API boundaries.
9. Keep heavy GIS preprocessing offline/precomputed; do not require DEM processing at runtime.
10. Demo Mode must work without internet.
11. Treat flood-risk output as decision support, not a guaranteed prediction.
12. Avoid adding dependencies unless they solve a concrete MVP requirement.
13. Do not replace working code merely for stylistic reasons.
14. Before declaring a task complete, run the relevant tests, static checks, and build checks.
15. When a dependency cannot be reliably installed or run in the target environment, implement a clean adapter/interface and a deterministic fallback rather than blocking the entire product.

## Product truth
The prototype should demonstrate:
- rainfall-driven risk escalation
- terrain/elevation-aware risk visualization
- estimated hazard arrival vs evacuation time
- dynamic safe-route recalculation when roads become unsafe
- citizen SOS / blockage reports
- offline/demo operation
- administrative command dashboard

The following are optional adapters, not blockers:
- real BLE mesh
- real Android/iOS barometer background sensing
- real bridge CCTV inference
- real acoustic TinyML inference
- live DEM processing

For optional hardware/ML integrations, provide interfaces and simulated inputs so the end-to-end product remains demonstrable.

## Scientific guardrails
Do NOT use atmospheric pressure drop as a primary flash-flood predictor. If represented in the UI, label it as an auxiliary sensor signal.
Do NOT assert that TRISHUL universally predicts flash floods 15 minutes in advance. Use language such as "estimated hazard arrival" and "localized risk assessment".
Do NOT invent model accuracy, training metrics, sensor performance, or emergency-service endorsements.

## Preferred architecture
Monorepo:
- `mobile/` — Flutter citizen application
- `backend/` — FastAPI API and risk/routing services
- `dashboard/` — administrative dashboard; prefer a lightweight web implementation unless an existing dashboard framework is clearly justified
- `data/` — small demo datasets only; never commit huge raw DEM/map datasets
- `scripts/` — preprocessing and demo-data generation
- `docs/` — product and technical documentation
- `tests/` — cross-component or fixture tests where appropriate

Backend modules should separate:
- API routes
- domain models
- risk engine
- routing engine
- report/SOS service
- demo scenario service
- data adapters

Flutter should separate:
- screens/widgets
- state management
- API client
- local persistence
- map/routing presentation
- demo mode
- emergency/report flows

## MVP priorities
P0: end-to-end demo
1. FastAPI backend
2. deterministic risk engine
3. scenario controls
4. safe route computation / route pruning
5. Flutter home/risk/map/report screens
6. admin dashboard
7. Demo Mode
8. tests and documentation

P1:
- offline cache
- local SQLite persistence
- report synchronization abstraction
- shelter management

P2:
- real BLE/Wi-Fi Direct
- acoustic model
- YOLO bridge vision
- native barometer integration
- real-time external data ingestion

## Risk engine baseline
Inputs should support at minimum:
- rainfall intensity
- cumulative/upstream rainfall
- terrain/slope risk
- soil saturation or proxy
- observed water/torrent signal
- road/bridge blockage reports

Return:
- risk score in [0, 1]
- risk level: LOW/MODERATE/HIGH/EXTREME
- confidence/quality metadata
- estimated hazard arrival minutes
- estimated evacuation minutes when route/user data exists
- recommended action

Make the weighting configurable and document it. For the prototype, a transparent weighted scoring model is preferable to an untrained XGBoost model pretending to be production ML.

## Routing baseline
Use a graph abstraction compatible with NetworkX/OSM-derived data. Each edge should have distance, elevation/slope metadata when available, and flood/closure status. Unsafe edges are removed or heavily penalized. Compute a route to a high-ground shelter. Precompute graph fixtures for demo use.

## Demo Mode
Demo Mode must provide deterministic scenarios:
- NORMAL
- HEAVY_RAIN
- FLASH_FLOOD
- ROAD_BLOCKED
- CELLULAR_OUTAGE

Demo Mode must allow the stage presentation to reproduce the same results every time.

## UI direction
Emergency-focused, modern, high contrast, clean typography, map-first. Avoid childish visuals and excessive gradients. Use clear severity colors consistently. All critical warnings must remain understandable without color alone.

## Git discipline
- Make small, coherent commits.
- Do not rewrite history.
- Do not delete user work without explicit reason.
- Commit messages should explain intent.
- Keep the default branch buildable.

## Completion protocol
After implementation:
1. run backend tests
2. run Flutter analyzer/tests/build checks available in the environment
3. run dashboard checks
4. verify Demo Mode manually or with automated tests
5. update documentation
6. report exactly what works, what is simulated, and any remaining limitations
