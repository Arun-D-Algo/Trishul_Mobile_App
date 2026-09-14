# Architecture Decisions, Assumptions and Open Questions

## Decisions

### D1 — Modular monolith
Chosen for hackathon speed, simple deployment and two-person ownership.

### D2 — Transparent risk baseline
Chosen before ML because a deterministic, explainable prototype is more defensible than an unvalidated trained model.

### D3 — XGBoost is optional P2
Use only with a legitimate dataset and reproducible evaluation. Never invent metrics.

### D4 — Precompute terrain
Chosen because DEM hydrology is computationally expensive and the prototype uses a defined corridor.

### D5 — Offline-first
Chosen because disaster scenarios may involve network failure.

### D6 — Satellite as augmentation
Satellite observations are useful confirmation/augmentation but are not guaranteed at the exact moment of a flash flood.

### D7 — Optional sensor adapters
Acoustic, barometer, CCTV/YOLO and BLE should be replaceable modules, not hard blockers.

### D8 — Demo Mode is mandatory
A deterministic offline scenario is required for stage reliability.

## Assumptions
- the prototype corridor is configurable
- demo map/terrain data is representative only
- shelter locations are demo data unless verified from authoritative sources
- hazard-arrival estimates are scenario estimates, not certified forecasts

## Open questions
- final demo corridor
- final map provider
- whether PostGIS is justified
- whether a legitimate flood dataset is available for a real ML model
- whether real BLE hardware is feasible within the remaining time
