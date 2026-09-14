# Backend API Contract

Backend: Python + FastAPI, modular monolith.

## Endpoints
- `GET /api/v1/health`
- `GET /api/v1/risk?lat=&lon=&horizon=`
- `GET /api/v1/risk/timeline?lat=&lon=`
- `GET /api/v1/weather?lat=&lon=`
- `GET /api/v1/layers/risk`
- `GET /api/v1/layers/flood`
- `GET /api/v1/layers/roads`
- `GET /api/v1/layers/reports`
- `POST /api/v1/routes/evacuate`
- `POST /api/v1/reports`
- `GET /api/v1/reports`
- `POST /api/v1/roads/{edge_id}/status`
- `GET /api/v1/shelters`
- `GET /api/v1/demo/{scenario}`

## Risk response
```json
{
  "location": {"lat": 0.0, "lon": 0.0},
  "risk_score": 0.78,
  "risk_level": "HIGH",
  "confidence": 0.76,
  "hazard_arrival_minutes": 18,
  "evacuation_minutes": 12,
  "recommended_action": "MOVE_TO_HIGH_GROUND",
  "data_quality": "demo",
  "generated_at": "ISO-8601"
}
```

Use Pydantic models. Keep schemas backwards-compatible once mobile/dashboard integration starts.

## Spatial layers
Return GeoJSON FeatureCollections for map layers. Keep geometry payloads small enough for mobile/demo use.
