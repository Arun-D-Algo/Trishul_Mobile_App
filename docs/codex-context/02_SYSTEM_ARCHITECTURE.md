# System Architecture

```text
Weather / Terrain / Incidents / Optional Sensors
                    |
              Data Adapters
                    |
             Normalization
                    |
              Feature Engine
                    |
          +---------+---------+
          |                   |
      Risk Engine        Routing Engine
          |                   |
          +---------+---------+
                    |
                 FastAPI
              /           \
         Flutter        Dashboard

Offline mobile cache and deterministic Demo Mode sit alongside the online path.
```

## Backend modular monolith
Modules:
- `api`
- `domain`
- `risk`
- `routing`
- `reports`
- `demo`
- `adapters`
- `persistence`

## External data rule
Provider-specific response formats must never leak into domain logic. Convert provider data into canonical internal models.

## Runtime principle
Do not run expensive DEM hydrology or large downloads in request handlers. Precompute small demo-region artifacts.

## Optional sources
The architecture can later accept acoustic observations, pressure deltas, bridge vision, satellite evidence, and BLE reports through adapters.
