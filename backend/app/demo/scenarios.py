from backend.app.schemas.common import ScenarioName
from backend.app.schemas.demo import ScenarioState, ScenarioSummary
from backend.app.schemas.risk import RiskInputs


_SCENARIOS: dict[ScenarioName, ScenarioState] = {
    ScenarioName.NORMAL: ScenarioState(
        name=ScenarioName.NORMAL,
        description="Baseline demo state with low rainfall and passable roads.",
        risk_inputs=RiskInputs(
            rainfall_intensity_mm_hr=4.0,
            cumulative_rainfall_mm_24h=18.0,
            slope_degrees=18.0,
            soil_saturation=0.25,
            observed_water_level=0.10,
            blockage_report_count=0,
        ),
        connectivity_online=True,
        blocked_edges=[],
    ),
    ScenarioName.HEAVY_RAIN: ScenarioState(
        name=ScenarioName.HEAVY_RAIN,
        description="Sustained heavy rainfall increases runoff and soil saturation.",
        risk_inputs=RiskInputs(
            rainfall_intensity_mm_hr=34.0,
            cumulative_rainfall_mm_24h=125.0,
            slope_degrees=26.0,
            soil_saturation=0.78,
            observed_water_level=0.55,
            blockage_report_count=0,
        ),
        connectivity_online=True,
        blocked_edges=[],
    ),
    ScenarioName.FLASH_FLOOD: ScenarioState(
        name=ScenarioName.FLASH_FLOOD,
        description="Severe rainfall and observed torrent signal create urgent demo risk.",
        risk_inputs=RiskInputs(
            rainfall_intensity_mm_hr=62.0,
            cumulative_rainfall_mm_24h=190.0,
            slope_degrees=34.0,
            soil_saturation=0.95,
            observed_water_level=0.92,
            blockage_report_count=2,
        ),
        connectivity_online=True,
        blocked_edges=[],
    ),
    ScenarioName.ROAD_BLOCKED: ScenarioState(
        name=ScenarioName.ROAD_BLOCKED,
        description="Primary route edge is blocked; routing should choose an alternate path.",
        risk_inputs=RiskInputs(
            rainfall_intensity_mm_hr=24.0,
            cumulative_rainfall_mm_24h=88.0,
            slope_degrees=25.0,
            soil_saturation=0.66,
            observed_water_level=0.52,
            blockage_report_count=1,
        ),
        connectivity_online=True,
        blocked_edges=["road-b-to-shelter"],
    ),
    ScenarioName.CELLULAR_OUTAGE: ScenarioState(
        name=ScenarioName.CELLULAR_OUTAGE,
        description="Connectivity outage demo; physical flood inputs stay similar to heavy rain.",
        risk_inputs=RiskInputs(
            rainfall_intensity_mm_hr=26.0,
            cumulative_rainfall_mm_24h=96.0,
            slope_degrees=25.0,
            soil_saturation=0.68,
            observed_water_level=0.48,
            blockage_report_count=0,
        ),
        connectivity_online=False,
        blocked_edges=[],
    ),
}


def list_scenarios() -> list[ScenarioSummary]:
    return [
        ScenarioSummary(name=scenario.name, description=scenario.description)
        for scenario in _SCENARIOS.values()
    ]


def get_scenario_state(scenario: ScenarioName) -> ScenarioState:
    return _SCENARIOS[scenario]
