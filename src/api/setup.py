from fastapi import FastAPI

from src.api.health import router as health_check_router


def setup_routes(app: FastAPI) -> None:
    app.include_router(health_check_router)
