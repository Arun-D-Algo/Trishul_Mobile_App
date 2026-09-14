from typing import Protocol

from backend.app.schemas.common import Location, ScenarioName
from backend.app.schemas.risk import RiskInputs


class WeatherProvider(Protocol):
    def get_risk_inputs(self, location: Location, scenario: ScenarioName) -> RiskInputs:
        """Return canonical weather/observation inputs for risk evaluation."""


class DemoWeatherProvider:
    def get_risk_inputs(self, location: Location, scenario: ScenarioName) -> RiskInputs:
        from backend.app.demo.scenarios import get_scenario_state

        return get_scenario_state(scenario).risk_inputs

