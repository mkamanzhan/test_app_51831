from fastapi import APIRouter
from pydantic import BaseModel, Field

from src.core.datetime import utc_now

router = APIRouter()


class HealthCheckResponse(BaseModel):
    status: str = Field(
        description="The status of the health check endpoint",
        examples=["ok"],
    )
    time: float = Field(
        description="The current UTC timestamp in seconds",
        examples=[utc_now().timestamp()],
    )


@router.get("/health")
async def health_check_endpoint() -> HealthCheckResponse:
    return HealthCheckResponse(
        status="ok",
        time=utc_now().timestamp(),
    )
