# Deterministic Demo Mode

## Purpose
The SIH presentation must work if internet, weather providers, satellite services, map tiles or optional sensors fail.

## Required scenarios
### NORMAL
- low rainfall
- low soil saturation
- LOW risk

### HEAVY_RAIN
- rainfall increases
- soil saturation rises
- HIGH risk

### FLASH_FLOOD
- severe rainfall and terrain/runoff signals
- EXTREME risk
- short estimated hazard arrival
- evacuation warning

### ROAD_BLOCKED
- primary route edge is unsafe
- routing engine selects alternate safe path

### CELLULAR_OUTAGE
- app switches to cached state
- report/SOS is queued locally
- last-updated information remains visible

## Demo controls
Provide reset and scenario selection. Use deterministic fixtures so the same input produces the same output.

Never describe simulated observations as live measurements.
