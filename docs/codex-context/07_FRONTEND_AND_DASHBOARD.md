# Frontend and Command Dashboard

## Dashboard
Preferred: Next.js + TypeScript + Tailwind + MapLibre if the team can support it quickly. A simpler React/web implementation is acceptable. Do not let map-provider setup block the demo.

Dashboard must show:
- command-center map
- risk legend
- current risk
- rainfall and timeline
- active alerts
- impacted roads/bridges
- incidents/reports
- shelters
- scenario controls

## Citizen app
Flutter + Dart.

Screens:
- Home/risk
- Map/evacuation
- Shelter details
- Report hazard
- SOS
- Offline/sync status
- Settings/demo mode

## UX principles
Emergency-first, high contrast, readable typography, minimal decoration. Warnings must be understandable without color alone. Show DEMO/SIMULATED labels whenever applicable.

## State handling
Frontend state should come from API/domain responses. Do not reproduce risk formulas or routing algorithms in TypeScript/Dart.
