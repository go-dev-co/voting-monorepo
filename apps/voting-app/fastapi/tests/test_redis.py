import pytest
from src.redis_functions import create_redis_instance
import os


@pytest.fixture
def redis_client():
    os.environ["REDIS_HOST"] = "localhost"
    os.environ["REDIS_PORT"] = "6379"
    os.environ["REDIS_CHANNEL"] = "votes"
    os.environ["REDIS_PASSWORD"] = "password"
    os.environ["REDIS_USERNAME"] = "username"

    client = create_redis_instance(os.environ["REDIS_HOST"],
                                   os.environ["REDIS_PORT"],
                                   os.environ["REDIS_CHANNEL"],
                                   os.environ["REDIS_PASSWORD"],
                                   username=os.environ["REDIS_USERNAME"])

    yield client
    client.close()


def test_redis_connection(redis_client):
    try:
        response = redis_client.ping()
        assert response is True
    except Exception as e:
        pytest.fail(f"Error connecting to redis: {e}")
