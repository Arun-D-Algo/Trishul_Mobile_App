from datetime import datetime

from pydantic import BaseModel, Field

from backend.app.schemas.common import Location, RecommendedAction, RiskLevel, ScenarioName


class RiskFactor(BaseModel):
    name: str
    raw_value: float
    normalized_value: float = Field(ge=0.0, le=1.0)
    weight: float = Field(ge=0.0, le=1.0)
    contribution: float = Field(ge=0.0, le=1.0)
    explanation: str


class RiskInputs(BaseModel):
    rainfall_intensity_mm_hr: float = Field(ge=0.0)
    cumulative_rainfall_mm_24h: float = Field(ge=0.0)
    slope_degrees: float = Field(ge=0.0, le=90.0)
    soil_saturation: float = Field(ge=0.0, le=1.0)
    observed_water_level: float = Field(ge=0.0, le=1.0)
    blockage_report_count: int = Field(ge=0)


class RiskResponse(BaseModel):
    location: Location
    risk_score: float = Field(ge=0.0, le=1.0)
    risk_level: RiskLevel
    confidence: float = Field(ge=0.0, le=1.0)
    hazard_arrival_minutes: int | None
    evacuation_minutes: int | None = None
    recommended_action: RecommendedAction
    data_quality: str
    scenario: ScenarioName
    generated_at: datetime
    factors: list[RiskFactor]
    assumptions: list[str]

