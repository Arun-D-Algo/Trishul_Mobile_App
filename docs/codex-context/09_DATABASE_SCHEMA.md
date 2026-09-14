# Database Schema

The original concept proposed PostgreSQL + PostGIS. For a one-week prototype, use PostgreSQL/PostGIS only if it can be set up quickly; otherwise use SQLite for the backend demo while preserving a clean repository/service layer.

## Logical entities
- `locations`: id, name, geometry, elevation
- `weather_observations`: timestamp, location, rainfall, soil moisture, temperature, humidity, source, quality
- `risk_predictions`: location, prediction time, horizon, probability, score, level, confidence, model version, quality
- `shelters`: id, name, geometry, elevation, capacity, status
- `road_edges`: id, geometry, distance, travel time, slope, status
- `incident_reports`: id/UUID, type, timestamp, geometry, payload, verification, sync status

Do not add Redis, PostGIS or complex distributed persistence unless the implementation gains a concrete benefit from it. Demo Mode may use deterministic fixtures instead of a database.
