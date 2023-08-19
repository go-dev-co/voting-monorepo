

from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)
valid_header = {
    "X-User-Hash": "12345678901234567890123456789012"
}


def test_get_root(redis_client):

    response = client.get("/", headers=valid_header)
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI"}


def test_post_vote_cats(redis_client):

    response = client.post(
        "/vote", json={"vote": "cats"}, headers=valid_header)
    assert response.status_code == 200
    assert response.json() == {"vote": "cats"}


def test_post_vote_dogs(redis_client):

    response = client.post(
        "/vote", json={"vote": "dogs"}, headers=valid_header)
    assert response.status_code == 200
    assert response.json() == {"vote": "dogs"}


def test_post_vote_invalid(redis_client):

    response = client.post(
        "/vote", json={"vote": "invalid"}, headers=valid_header)
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid submission"}


def test_valid_user_hash(redis_client):

    response = client.post(
        "/vote", json={"vote": "cats"}, headers=valid_header)
    assert response.status_code == 200
    assert response.json() == {"vote": "cats"}
