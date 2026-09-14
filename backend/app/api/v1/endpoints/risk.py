from fastapi import APIRouter, Query

from backend.app.adapters.weather import DemoWeatherProvider
from backend.app.core.config import get_settings
from backend.app.schemas.common import Location, ScenarioName
from backend.app.schemas.risk import RiskResponse
from backend.app.risk.engine import evaluate_risk

router = APIRouter()


@router.get("", response_model=RiskResponse)
def current_risk(
    lat: float = Query(..., ge=-90.0, le=90.0),
    lon: float = Query(..., ge=-180.0, le=180.0),
    horizon: int = Query(60, ge=15, le=360),
    scenario: ScenarioName | None = None,
) -> RiskResponse:
    del horizon
    settings = get_settings()
    selected = scenario or ScenarioName(settings.default_scenario)
    location = Location(lat=lat, lon=lon)
    inputs = DemoWeatherProvider().get_risk_inputs(location, selected)
    return evaluate_risk(location=location, inputs=inputs, scenario=selected)


@router.get("/current", response_model=RiskResponse)
def current_default_risk() -> RiskResponse:
    location = Location(lat=30.3165, lon=78.0322)
    scenario = ScenarioName(get_settings().default_scenario)
    inputs = DemoWeatherProvider().get_risk_inputs(location, scenario)
    return evaluate_risk(location=location, inputs=inputs, scenario=scenario)

