from fastapi import FastAPI

from src.api.setup import setup_routes
from src.configs import configs
from src.core.logging import init_logger
from src.pipelines.calculate_phrases_distance import (
    run_pipeline as run_calculate_phrases_distance_pipeline,
)
from src.pipelines.clean_phrases import run_pipeline as run_clean_phrases_pipeline


def get_app() -> FastAPI:
    init_logger(level=configs.logging.level)

    app = FastAPI(
        title=configs.title,
        debug=configs.fast_api.debug,
    )
    setup_routes(app)

    return app


def run_pipeline(name: str) -> None:
    pipelines_map = {
        "clean_phrases": run_clean_phrases_pipeline,
        "calculate_phrases_distance": run_calculate_phrases_distance_pipeline,
    }

    pipeline = pipelines_map.get(name)
    if pipeline is None:
        raise ValueError(f"Unknown pipeline name: {name}")

    pipeline()
