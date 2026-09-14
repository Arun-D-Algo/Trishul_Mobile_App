from fastapi import APIRouter

from backend.app.core.config import get_settings
from backend.app.schemas.common import utc_now
from backend.app.schemas.health import HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    settings = get_settings()
    return HealthResponse(
        status="ok",
        service="trishul-backend",
        version="0.1.0",
        environment=settings.environment,
        demo_mode=settings.demo_mode,
        generated_at=utc_now(),
    )

