import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


# Tests functions for testing the middleware,


# utilize the root endpoint for generic middleware testing

# Test the roo


def test_invalid_user_hash_empty():
    with pytest.raises(HTTPException) as exc_info:
        client.get("/")

    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Invalid submission: No unique user hash \
            provided"


def test_invalid_user_hash_short():
    with pytest.raises(HTTPException) as exec_info:
        client.get(
            "/", headers={"X-User-Hash": "1234567890123456789012345678901"})
    assert exec_info.value.status_code == 401
    assert exec_info.value.detail == "Invalid submission: Unique user hash \
                invalid"
