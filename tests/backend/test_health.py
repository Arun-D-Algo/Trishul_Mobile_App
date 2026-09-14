from fastapi.testclient import TestClient

from backend.app.main import create_app


def test_health_endpoint_returns_demo_safe_metadata() -> None:
    client = TestClient(create_app())

    response = client.get("/api/v1/health")

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["service"] == "trishul-backend"
    assert payload["demo_mode"] is True

