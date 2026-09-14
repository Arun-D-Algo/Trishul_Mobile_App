from fastapi.testclient import TestClient

from backend.app.demo.scenarios import get_scenario_state
from backend.app.risk.engine import evaluate_risk
from backend.app.schemas.common import Location, ScenarioName


def test_flash_flood_risk_is_higher_than_normal() -> None:
    location = Location(lat=30.3165, lon=78.0322)
    normal = evaluate_risk(
        location=location,
        inputs=get_scenario_state(ScenarioName.NORMAL).risk_inputs,
        scenario=ScenarioName.NORMAL,
    )
    flash_flood = evaluate_risk(
        location=location,
        inputs=get_scenario_state(ScenarioName.FLASH_FLOOD).risk_inputs,
        scenario=ScenarioName.FLASH_FLOOD,
    )

    assert flash_flood.risk_score > normal.risk_score
    assert flash_flood.risk_level == "EXTREME"
    assert flash_flood.hazard_arrival_minutes is not None
    assert flash_flood.hazard_arrival_minutes < 30


def test_risk_endpoint_uses_requested_demo_scenario() -> None:
    client = TestClient(__import__("backend.app.main", fromlist=["create_app"]).create_app())

    response = client.get(
        "/api/v1/risk",
        params={"lat": 30.3165, "lon": 78.0322, "scenario": "HEAVY_RAIN"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["scenario"] == "HEAVY_RAIN"
    assert payload["risk_level"] in {"HIGH", "EXTREME"}
    assert payload["data_quality"] == "demo"


def test_invalid_latitude_is_rejected() -> None:
    client = TestClient(__import__("backend.app.main", fromlist=["create_app"]).create_app())

    response = client.get("/api/v1/risk", params={"lat": 120, "lon": 78.0322})

    assert response.status_code == 422

