import logging
import pytest
import os


@pytest.fixture(scope="session", autouse=True)
def redis_client():
    os.environ["REDIS_HOST"] = "localhost"
    os.environ["REDIS_PORT"] = "6379"
    os.environ["REDIS_CHANNEL"] = "votes"
    os.environ["REDIS_PASSWORD"] = "password"
    os.environ["REDIS_USERNAME"] = "username"


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    logging.basicConfig(level=logging.ERROR,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filename='error.log',
                        filemode='a')
