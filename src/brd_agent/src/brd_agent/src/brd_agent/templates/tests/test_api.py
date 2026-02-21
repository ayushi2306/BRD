from fastapi.testclient import TestClient

from brd_agent.api import app


client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_generate_endpoint() -> None:
    payload = {
        "company_name": "Acme Corp",
        "industry": "ecommerce",
        "product_name": "Acme Store",
        "target_customers": "D2C brands",
    }

    response = client.post("/generate", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert "markdown" in data
    assert "Business Requirements Document" in data["markdown"]
