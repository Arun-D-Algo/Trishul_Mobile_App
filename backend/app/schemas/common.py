from datetime import UTC, datetime
from enum import StrEnum

from pydantic import BaseModel, Field


class ScenarioName(StrEnum):
    NORMAL = "NORMAL"
    HEAVY_RAIN = "HEAVY_RAIN"
    FLASH_FLOOD = "FLASH_FLOOD"
    ROAD_BLOCKED = "ROAD_BLOCKED"
    CELLULAR_OUTAGE = "CELLULAR_OUTAGE"


class RiskLevel(StrEnum):
    LOW = "LOW"
    MODERATE = "MODERATE"
    HIGH = "HIGH"
    EXTREME = "EXTREME"


class RecommendedAction(StrEnum):
    MONITOR = "MONITOR"
    PREPARE_TO_EVACUATE = "PREPARE_TO_EVACUATE"
    MOVE_TO_HIGH_GROUND = "MOVE_TO_HIGH_GROUND"
    EVACUATE_NOW = "EVACUATE_NOW"


class Location(BaseModel):
    lat: float = Field(ge=-90.0, le=90.0)
    lon: float = Field(ge=-180.0, le=180.0)


def utc_now() -> datetime:
    return datetime.now(UTC)

