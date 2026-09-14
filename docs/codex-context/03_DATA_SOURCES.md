# Data Sources and Adapter Contracts

## Principle
External providers are dependencies, not application logic. Every provider exposes canonical internal data.

## Weather
Preferred prototype provider: Open-Meteo. Canonical fields may include latitude, longitude, timestamp, precipitation/rain, precipitation probability, temperature, humidity, soil moisture, source and quality.

Use a deterministic DemoWeatherProvider when offline or when the external service is unavailable.

## Terrain
Preferred sources include Copernicus DEM or SRTM. For the MVP, use preprocessed terrain fixtures for the selected demo corridor.

Derived features:
- elevation
- slope
- flow direction
- flow accumulation
- drainage density
- distance to stream

## Roads
Use OSM-derived data when practical, but store a compact demo graph. Runtime routing must not depend on downloading OSM.

## Citizen reports
Canonical report types:
- FLOOD
- BLOCKED_ROAD
- BRIDGE_FLOODED
- LANDSLIDE
- SOS

Reports have UUID, timestamp, location, type, payload, source, verification status and sync state.

## Optional sources
Acoustic, barometer, bridge vision, satellite and peer-to-peer observations should implement adapters. They are not required for the core demo.
