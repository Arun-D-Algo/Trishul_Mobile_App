# TRISHUL 2.0 Product Specification

## 1. Problem
SIH26192 — Ministry of Home Affairs, Disaster Management. Flash floods in mountainous terrain can develop rapidly and disrupt sensors, roads, and communications. TRISHUL provides localized risk assessment, warnings, evacuation routing, and resilient citizen reporting.

## 2. Target users
- Residents in hilly catchments
- Trekkers and tourists
- District Disaster Management Authorities
- Search and rescue teams

## 3. Prototype promise
TRISHUL combines rainfall, terrain, local observations, and road status to produce a transparent risk assessment and a safe evacuation recommendation. The prototype is designed for demonstration and decision support; it is not a certified emergency-warning system.

## 4. Main user journeys

### Citizen
1. Open app.
2. See current location/elevation zone and risk level.
3. See risk score, contributing factors, and estimated hazard-arrival time.
4. If evacuation is required, see nearest suitable shelter and route.
5. If a road/bridge is unsafe, submit a one-tap report.
6. In Demo Mode/offline conditions, the app continues to show cached scenario data.

### Authority
1. Open dashboard.
2. See catchment risk and active reports.
3. Change rainfall/scenario inputs.
4. Observe risk and affected routes update.
5. Mark a road or bridge unsafe.
6. Verify that citizen route recalculates.

## 5. Core screens

### Mobile
- Splash / onboarding
- Home / risk overview
- Flood map
- Evacuation route
- Report incident
- SOS / emergency contacts
- Settings / Demo Mode / connectivity status

### Dashboard
- Overview KPI cards
- Catchment/risk map
- Rainfall scenario controls
- Active citizen reports
- Road/bridge status
- Shelters
- Event timeline

## 6. Risk model
For the prototype, use an explainable normalized scoring model rather than an untrained ML model. Example inputs:

`risk = weighted(rainfall, cumulative_rainfall, slope, soil_saturation_proxy, observed_water_signal, blockage_signal)`

Normalize each input to [0,1]. Keep weights in configuration. Clamp the final score to [0,1]. Suggested initial weights:
- rainfall intensity: 0.30
- cumulative/upstream rainfall: 0.20
- slope/topographic exposure: 0.15
- soil saturation proxy: 0.10
- observed water/torrent signal: 0.20
- verified blockage/incident signal: 0.05

These weights are prototype assumptions, not scientific calibration. Clearly document them.

Risk bands:
- 0.00–0.24 LOW
- 0.25–0.49 MODERATE
- 0.50–0.74 HIGH
- 0.75–1.00 EXTREME

Actions:
- LOW: monitor conditions
- MODERATE: stay alert and review evacuation route
- HIGH: prepare to evacuate / avoid low-lying stream crossings
- EXTREME: evacuate toward designated safe shelter if instructed

## 7. Hazard-arrival estimate
Use a transparent prototype estimate derived from upstream distance and modeled flow velocity / scenario configuration. It is an estimate for the demo, not a physically validated hydrodynamic simulation.

`T_HA = upstream_distance / assumed_effective_flow_speed`

Keep units explicit and clamp unreasonable values.

## 8. Evacuation time
Estimate from route distance and configured walking speed:

`T_RE = route_distance / evacuation_speed`

If `T_HA <= T_RE`, show a critical warning because the estimated hazard arrival time is no greater than the estimated evacuation time.

## 9. Routing
Use a graph containing roads/paths and shelters. Edge attributes should include:
- distance
- elevation gain/loss when available
- slope penalty when available
- flood status
- blockage status

Safe route cost should prioritize safety over raw shortest distance. Unsafe edges must be excluded in the default safe-routing mode.

## 10. Reports
A report should contain:
- id
- type: FLOOD / BLOCKED_ROAD / BRIDGE / LANDSLIDE / OTHER
- latitude/longitude
- timestamp
- severity
- optional note
- source: citizen / sensor / authority / demo
- verification state

Prototype aggregation can use time decay and spatial clustering. Do not escalate from a single unverified report unless Demo Mode explicitly asks for it.

## 11. Offline / resilience behavior
The product must distinguish:
- ONLINE
- OFFLINE
- DEMO

Cached maps/scenarios remain readable offline. Reports are stored locally and queued for synchronization. The first prototype may simulate mesh propagation through a local sync abstraction; the UI must make it clear when a report was received peer-to-peer versus from the backend.

## 12. Optional integrations
Implement behind interfaces:
- Open-Meteo adapter
- DEM/OSM preprocessing adapter
- acoustic classifier adapter
- bridge-vision adapter
- native barometer adapter
- BLE/Wi-Fi Direct transport adapter

The absence of these integrations must never prevent the main demo from running.

## 13. Demo scenarios
### NORMAL
Low rainfall, no incidents, normal route.
### HEAVY_RAIN
High rainfall raises risk to HIGH; route remains available.
### FLASH_FLOOD
Risk reaches EXTREME; hazard-arrival estimate becomes short; evacuation warning appears.
### ROAD_BLOCKED
A bridge/road edge becomes unsafe; route recalculates through an elevated alternative.
### CELLULAR_OUTAGE
Backend unavailable; cached map and local report queue remain functional; peer-sync UI can demonstrate simulated transfer.

## 14. Acceptance criteria
The prototype is successful when a judge can:
1. Open the citizen app.
2. See a meaningful risk level.
3. Change the scenario/rainfall in the dashboard.
4. Watch risk update.
5. Mark a road blocked.
6. See the evacuation route change.
7. Submit a citizen incident.
8. Switch to offline/demo mode and still operate the core flow.
9. Understand why the system produced its warning.
