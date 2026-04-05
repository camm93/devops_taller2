import pytest
from application import application


@pytest.fixture
def client():
    # This sets up a "virtual" version of your app to test without running a server
    application.config["TESTING"] = True
    with application.test_client() as client:
        yield client


def test_index_route(client):
    """Test that the home route returns a 200 OK status."""
    response = client.get("/")
    assert response.status_code == 200


def test_data_is_json(client):
    """Test that the response is actually JSON."""
    response = client.get("/")
    assert response.is_json
