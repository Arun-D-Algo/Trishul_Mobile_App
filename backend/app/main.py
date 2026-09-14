from fastapi import FastAPI

from backend.app.api.v1.router import api_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="TRISHUL 2.0 Backend",
        description="Decision-support backend for deterministic flash-flood risk demos.",
        version="0.1.0",
    )
    app.include_router(api_router)
    return app


app = create_app()

