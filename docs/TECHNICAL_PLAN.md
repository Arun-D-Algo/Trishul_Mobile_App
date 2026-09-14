# TRISHUL 2.0 Technical Implementation Plan

## Repository layout

```text
.
├── AGENTS.md
├── README.md
├── docs/
│   ├── PRODUCT_SPEC.md
│   ├── TECHNICAL_PLAN.md
│   └── DEMO_SCRIPT.md
├── mobile/
├── backend/
├── dashboard/
├── scripts/
├── data/
└── tests/
```

## Backend
Python 3.11+ and FastAPI.

Suggested dependencies:
- fastapi
- uvicorn
- pydantic / pydantic-settings
- networkx
- numpy
- httpx
- pytest

Optional dependencies should be isolated where possible:
- osmnx
- rasterio
- geopandas
- pysheds
- xgboost

API endpoints:

`GET /health`

`GET /api/v1/scenarios`

`POST /api/v1/risk/evaluate`

`GET /api/v1/risk/current`

`POST /api/v1/routes/evacuate`

`POST /api/v1/reports`

`GET /api/v1/reports`

`POST /api/v1/roads/{edge_id}/status`

`GET /api/v1/shelters`

`GET /api/v1/demo/{scenario}`

Keep response schemas stable and versioned.

## Risk engine
Create a pure Python service with no FastAPI dependencies so it can be unit tested. Inputs and outputs should be Pydantic models at the API boundary and dataclasses/domain models internally if useful.

Implement:
- normalization
- weighted score
- severity banding
- action recommendation
- hazard arrival estimate
- evacuation comparison

Return contributing-factor explanations so the UI can show why risk changed.

## Routing engine
Use NetworkX. Keep a small deterministic fixture graph under `data/demo/` for development and stage demo.

Route objective:
1. exclude flooded/blocked edges
2. prefer lower hazard exposure
3. minimize travel distance/time among safe alternatives

Do not require live OSM downloads at runtime.

## Data layer
Create adapters:
- `WeatherProvider`
- `TerrainProvider`
- `IncidentProvider`
- `MapProvider`
- `SensorProvider`

Provide deterministic fake/demo implementations. Real providers can be added later without changing domain logic.

## Mobile
Flutter stable channel.

Suggested packages only when needed:
- `dio` or `http` for API
- `flutter_map` for map rendering if it reduces API/licensing friction
- `sqflite` for local persistence
- `shared_preferences` for lightweight settings
- `connectivity_plus` for network status
- `geolocator` for location

Do not require Mapbox tokens for the prototype unless already available. Prefer a map implementation that can work with cached/local tiles or demo geometry.

Mobile architecture:
- presentation
- application/state
- domain
- data/api
- data/local

The app should start in Demo Mode if no backend is configured, while clearly showing DEMO status.

## Dashboard
A lightweight React/Next.js or plain web dashboard is acceptable. If the existing environment makes Streamlit significantly faster, use Streamlit. The dashboard must communicate with the same FastAPI API rather than duplicate business logic.

Dashboard controls:
- scenario selector
- rainfall intensity
- cumulative rainfall
- observed torrent signal
- soil saturation proxy
- road closure toggle
- report verification

## Demo data
Create compact JSON/GeoJSON fixtures:
- one mountainous catchment
- 8–20 road/path nodes
- 1–3 shelters
- several river/stream segments
- 3–5 sample incident reports
- scenario configurations

Do not commit large raw satellite/DEM/map archives.

## Testing
Backend tests:
- score normalization
- risk bands
- hazard-arrival calculation
- evacuation warning condition
- safe route exists
- blocked route gets rejected
- alternative route selected
- report validation
- demo scenario determinism

Mobile tests:
- risk display
- scenario state update
- report creation
- offline queue behavior where feasible

## Environment variables
Provide `.env.example` with placeholders only:

```text
TRISHUL_ENV=development
TRISHUL_API_BASE_URL=http://localhost:8000
OPEN_METEO_ENABLED=false
MAP_PROVIDER=
MAP_API_KEY=
```

No secrets in source control.

## Build order
1. Create monorepo skeleton and docs.
2. Build backend domain models and deterministic demo data.
3. Build risk engine and tests.
4. Build routing engine and tests.
5. Build API endpoints.
6. Build dashboard controls.
7. Build Flutter citizen screens.
8. Connect Flutter to API.
9. Add local cache/offline behavior.
10. Add optional sensor/report adapters.
11. Polish Demo Mode.
12. Run complete verification and document limitations.

## What not to do during MVP
- Do not train a large neural network.
- Do not build a real hydrodynamic solver.
- Do not process a massive DEM at request time.
- Do not depend on paid map APIs.
- Do not make BLE mesh a hard dependency.
- Do not make live CCTV a hard dependency.
- Do not fabricate real sensor data as if it were measured.
- Do not spend the week on authentication/admin RBAC unless required.
