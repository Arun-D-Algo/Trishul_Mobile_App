# Product Requirements — TRISHUL 2.0

## Objective
Create a prototype early-warning and decision-support application for flash-flood-prone mountainous catchments.

## Resident/tourist journey
1. Open app.
2. Select current/demo location.
3. See localized risk and map.
4. See rainfall and hazard/evacuation time information.
5. Receive warning when risk crosses a threshold.
6. Open safe evacuation route.
7. If offline, use cached critical data and create SOS/report locally.
8. Sync queued reports when connectivity returns.

## DDMA journey
1. Open command dashboard.
2. View regional risk map.
3. Inspect a catchment/location.
4. See rainfall, terrain factors, risk score and explanation.
5. Inspect incidents and affected infrastructure.
6. Change a demo scenario or rainfall input.
7. Observe risk and routing changes.

## Core requirements
- risk score and severity
- contributing-factor explanation
- estimated hazard arrival
- evacuation-time comparison
- safe route to high ground
- road/bridge hazard updates
- shelter information
- citizen reports/SOS
- offline queue
- deterministic Demo Mode

## Non-goals for one-week MVP
- certified public warning system
- production emergency dispatch
- universal hydrodynamic simulation
- guaranteed prediction lead time
- production-grade BLE mesh
- large-scale real-time satellite processing
