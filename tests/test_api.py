from fastapi.testclient import TestClient
from mldeploy.main import app

client = TestClient(app)


def test_root():
    """Check that root endpoint is reachable."""
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.json()
    assert "ML model serving API" in data["message"]


def test_predict():
    """Check that prediction endpoint works."""
    payload = {"features": [5.1, 3.5, 1.4, 0.2]}  # valid Iris features
    resp = client.post("/predict", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert "prediction" in data
    assert isinstance(data["prediction"], int)
