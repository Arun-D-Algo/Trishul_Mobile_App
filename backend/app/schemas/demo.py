from pydantic import BaseModel

from backend.app.schemas.common import ScenarioName
from backend.app.schemas.risk import RiskInputs


class ScenarioSummary(BaseModel):
    name: ScenarioName
    description: str


class ScenarioState(BaseModel):
    name: ScenarioName
    description: str
    risk_inputs: RiskInputs
    connectivity_online: bool
    blocked_edges: list[str]

