from fastapi import APIRouter

from backend.app.demo.scenarios import get_scenario_state, list_scenarios
from backend.app.schemas.common import ScenarioName
from backend.app.schemas.demo import ScenarioState, ScenarioSummary

router = APIRouter()


@router.get("/scenarios", response_model=list[ScenarioSummary])
def scenarios() -> list[ScenarioSummary]:
    return list_scenarios()


@router.get("/{scenario}", response_model=ScenarioState)
def scenario_state(scenario: ScenarioName) -> ScenarioState:
    return get_scenario_state(scenario)

