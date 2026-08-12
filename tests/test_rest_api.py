import pytest

from api.app import app


@pytest.fixture
def client():

    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_health(client):

    response = client.get("/api/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "success"


def test_flight_price_prediction(client):

    payload = {

        "travel_code": 1001,

        "user_code": 1,

        "source": "Recife (PE)",

        "destination": "Florianopolis (SC)",

        "flight_type": "economic",

        "agency": "FlyingDrops",

        "day_of_week": "Friday",

        "time": 60,

        "distance": 500,

        "year": 2026,

        "month": 8,

        "day": 14,

        "week_of_year": 33
    }

    response = client.post(
        "/api/predict/flight-price",
        json=payload
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "success"

    assert "prediction" in data

    assert isinstance(
        data["prediction"],
        (int, float)
    )

    assert data["currency"] == "USD"