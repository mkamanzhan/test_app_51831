from fastapi.testclient import TestClient
from pytest_asyncio import fixture

from src.main import get_app


@fixture
async def test_client() -> TestClient:
    return TestClient(get_app())
