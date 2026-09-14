from fastapi import APIRouter

from backend.app.api.v1.endpoints import demo, health, risk

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(health.router, tags=["health"])
api_router.include_router(demo.router, prefix="/demo", tags=["demo"])
api_router.include_router(risk.router, prefix="/risk", tags=["risk"])

