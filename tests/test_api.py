from fastapi.testclient import TestClient

from app.main import app
import app.main as main

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_get_2026_holidays():
    response = client.post(
        "/v1/holidays",
        json={"year": 2026}
    )

    assert response.status_code == 200
    assert response.json()["dataset_available"] is True


def test_get_2027_holidays():
    response = client.post(
        "/v1/holidays",
        json={"year": 2027}
    )

    assert response.status_code == 200
    assert response.json()["dataset_available"] is True
    assert response.json()["dataset_status"] == "partial"


def test_unavailable_year():
    response = client.post(
        "/v1/holidays",
        json={"year": 2028}
    )

    assert response.status_code == 200
    assert response.json()["dataset_available"] is False


def test_check_public_holiday():
    response = client.post(
        "/v1/check-date",
        json={"date": "2026-01-01"}
    )

    assert response.status_code == 200
    assert response.json()["is_public_holiday"] is True


def test_check_2027_holiday():
    response = client.post(
        "/v1/check-date",
        json={"date": "2027-01-01"}
    )

    assert response.status_code == 200
    assert response.json()["is_public_holiday"] is True


def test_check_ordinary_day():
    response = client.post(
        "/v1/check-date",
        json={"date": "2026-11-19"}
    )

    assert response.status_code == 200
    assert response.json()["is_public_holiday"] is False


def test_working_day():
    response = client.post(
        "/v1/working-day",
        json={"date": "2026-11-19"}
    )

    assert response.status_code == 200
    assert response.json()["is_working_day"] is True


def test_weekend():
    response = client.post(
        "/v1/working-day",
        json={"date": "2026-11-21"}
    )

    assert response.status_code == 200
    assert response.json()["is_working_day"] is False


def test_invalid_year():
    response = client.post(
        "/v1/holidays",
        json={"year": 1800}
    )

    assert response.status_code == 422

def test_invalid_dataset_returns_500(monkeypatch):
    def mock_dataset(year):
        raise ValueError("Invalid dataset")

    monkeypatch.setattr(
        main,
        "get_holiday_dataset",
        mock_dataset
    )

    response = client.post(
        "/v1/holidays",
        json={"year": 2026}
    )

    assert response.status_code == 500
    assert "data validation error" in response.json()["detail"]


def test_unexpected_error_returns_500(monkeypatch):
    def mock_dataset(year):
        raise RuntimeError("Unexpected failure")

    monkeypatch.setattr(
        main,
        "get_holiday_dataset",
        mock_dataset
    )

    response = client.post(
        "/v1/holidays",
        json={"year": 2026}
    )

    assert response.status_code == 500
    assert response.json()["detail"] == "An unexpected server error occurred."