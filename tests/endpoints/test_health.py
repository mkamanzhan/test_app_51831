from fastapi.testclient import TestClient
from freezegun import freeze_time

from src.core.datetime import utc_now
from tests.constants import freezed_datetime


@freeze_time(freezed_datetime.isoformat())
async def test__health_check_endpoint(
    test_client: TestClient,
) -> None:
    response = test_client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "time": utc_now().timestamp(),
    }
