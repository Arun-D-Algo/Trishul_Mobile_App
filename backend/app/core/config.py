from functools import lru_cache
from os import getenv

from pydantic import BaseModel, Field


class Settings(BaseModel):
    """Environment-backed runtime settings with demo-safe defaults."""

    environment: str = Field(default="development", alias="TRISHUL_ENV")
    api_base_url: str = Field(default="http://localhost:8000", alias="TRISHUL_API_BASE_URL")
    demo_mode: bool = Field(default=True, alias="DEMO_MODE")
    default_scenario: str = Field(default="NORMAL", alias="DEFAULT_SCENARIO")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")
    open_meteo_enabled: bool = Field(default=False, alias="OPEN_METEO_ENABLED")
    weather_base_url: str = Field(default="https://api.open-meteo.com", alias="WEATHER_BASE_URL")
    model_path: str | None = Field(default=None, alias="MODEL_PATH")


def _as_bool(value: str | None, default: bool) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


@lru_cache
def get_settings() -> Settings:
    return Settings(
        TRISHUL_ENV=getenv("TRISHUL_ENV", "development"),
        TRISHUL_API_BASE_URL=getenv("TRISHUL_API_BASE_URL", "http://localhost:8000"),
        DEMO_MODE=_as_bool(getenv("DEMO_MODE"), True),
        DEFAULT_SCENARIO=getenv("DEFAULT_SCENARIO", "NORMAL"),
        LOG_LEVEL=getenv("LOG_LEVEL", "INFO"),
        OPEN_METEO_ENABLED=_as_bool(getenv("OPEN_METEO_ENABLED"), False),
        WEATHER_BASE_URL=getenv("WEATHER_BASE_URL", "https://api.open-meteo.com"),
        MODEL_PATH=getenv("MODEL_PATH") or None,
    )

