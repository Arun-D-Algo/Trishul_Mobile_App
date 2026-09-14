# TRISHUL 2.0 — Two-Person Team Split

## Team

### Arunangshu Dasgupta — Platform / Backend / GIS Lead
Owns the shared backend contract and the infrastructure that makes the product work.

Primary ownership:
- FastAPI application and Pydantic schemas
- Risk engine and risk-explanation logic
- Weather/data adapters
- GIS preprocessing and demo GeoJSON
- NetworkX evacuation graph and routing service
- Database models/migrations if persistence is used
- API integration tests
- Docker/dev environment
- Backend integration with dashboard/mobile

Codex working directory emphasis:
- `backend/`
- `scripts/`
- `data/`
- `tests/backend/`
- relevant `docs/`

### Rutuj Runwal — Product / Frontend / Mobile Lead
Owns the user-facing applications and offline emergency experience.

Primary ownership:
- Flutter citizen application
- Admin command dashboard
- Map/risk visualization
- Offline local storage and report queue
- SOS/report UX
- Demo controls and presentation polish
- Frontend/mobile tests
- API client integration

Codex working directory emphasis:
- `mobile/`
- `dashboard/`
- `tests/mobile/`
- `tests/dashboard/`

## Shared responsibility
Both teammates review:
- API contract changes
- data model changes
- security/privacy issues
- demo reliability
- scientific claims
- final integration

## Branch strategy
Use two feature branches:
- `feat/arunangshu-platform`
- `feat/rutuj-client`

Do not have both Codex sessions editing the same files at the same time.

Arunangshu owns shared backend/domain contracts first. Rutuj can build against documented mock JSON/API schemas immediately and switch to the real API once endpoints stabilize.

## Integration checkpoints
1. Backend schemas + demo fixtures agreed.
2. Risk endpoint works with deterministic scenarios.
3. Routing endpoint works with blocked-edge scenario.
4. Rutuj connects dashboard/mobile to the stable endpoints.
5. Offline report queue works independently of backend availability.
6. Final merge and end-to-end test.

## Deliberately deferred unless the core demo is stable
- production BLE mesh
- native background barometer sensing
- real CCTV/YOLO pipeline
- acoustic TinyML training
- live satellite processing
- large-scale DEM processing
- authentication/RBAC beyond what the demo genuinely needs

These should be implemented as adapter interfaces or simulated demo inputs before attempting real integrations.
