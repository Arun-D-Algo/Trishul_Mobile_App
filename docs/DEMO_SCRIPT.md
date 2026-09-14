# TRISHUL 2.0 — 3-Minute SIH Demo Script

## Objective
Demonstrate one complete story rather than disconnected features.

## 0:00–0:30 — Normal conditions
- Open citizen app.
- Show LOW/MODERATE risk.
- Show current location, safe route and nearest shelter.
- Open command dashboard.

Narration: "TRISHUL continuously combines rainfall, terrain and local observations into a transparent localized risk assessment."

## 0:30–1:15 — Heavy rainfall / flash-flood escalation
- Select HEAVY_RAIN or FLASH_FLOOD scenario.
- Increase rainfall intensity.
- Show risk score and severity increasing.
- Show contributing factors.
- Show estimated hazard-arrival time.
- If hazard arrival is less than or equal to evacuation time, show critical warning.

Narration: "The system does not just show a red map. It explains what changed and compares estimated hazard arrival with estimated evacuation time."

## 1:15–2:05 — Dynamic evacuation
- Mark the primary bridge/road as flooded.
- Show route becoming invalid.
- Recalculate route to high-ground shelter.
- Highlight the alternate elevated route.

Narration: "Instead of routing purely by distance, TRISHUL removes unsafe edges and recomputes a safer path."

## 2:05–2:40 — Citizen report / communications resilience
- On citizen app, submit BLOCKED_ROAD or FLOOD report.
- Show it appearing on dashboard.
- Switch to OFFLINE/CELLULAR_OUTAGE Demo Mode.
- Show report queued locally.
- Demonstrate simulated peer synchronization if implemented.

Narration: "The prototype separates local emergency data collection from internet connectivity, allowing information to be retained and synchronized when connectivity returns."

## 2:40–3:00 — Close
Show dashboard and mobile map together.

Closing line:
"TRISHUL is a network-resilient decision-support platform for the minutes when terrain, roads, sensors and connectivity become unreliable."

## Demo safety rules
- Never claim that demo data is real-time measured data.
- Never claim certified emergency-warning capability.
- Clearly label simulated sensor inputs.
- Keep one deterministic backup scenario ready if any live component fails.
