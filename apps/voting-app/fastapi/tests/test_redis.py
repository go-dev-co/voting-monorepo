
from src.redis_functions import create_redis_instance
import os
import redis
import logging
from redis.exceptions import ConnectionError


#     client = create_redis_instance(os.environ["REDIS_HOST"],
#                                    os.environ["REDIS_PORT"],
#                                    os.environ["REDIS_CHANNEL"],
#                                    password=os.environ["REDIS_PASSWORD"],
#                                    username=os.environ["REDIS_USERNAME"])

#     yield client
#     client.close()


# def test_redis_connection(redis_client):
#     try:
#         response = redis_client.ping()
#         assert response is True
#     except Exception as e:
#         pytest.fail(f"Error connecting to redis: {e}")

# Test if Reddis can be connected too locally
def test_redis_reachability(redis_client):
    try:
        r = redis.Redis()
        response = r.ping()
        r.close()
        assert response is not None
    except ConnectionError:
        print("Connection Error:")

# TestFunction: create_redis_instance
# Ensure that the connection behaves as expected


def test_function_create_redis_instance():
    try:
        logging.info("Connecting to known redis host...")
        knownRedis = redis.Redis(
            host=os.environ["REDIS_HOST"], port=os.environ["REDIS_PORT"],
            decode_responses=True, password=os.environ["REDIS_PASSWORD"]
        )
        knownResponse = knownRedis.ping()
        logging.info("Connection to known host successful")
        knownRedis.close()
    except ConnectionError as ce:
        logging.error(ce.strerror())
    try:
        logging.info("Using create_redis_instance() to connect to redis")
        newRedis = create_redis_instance(
            host=os.environ["REDIS_HOST"],
            port=os.environ["REDIS_PORT"],
            channel=os.environ["REDIS_CHANNEL"],
            password=os.environ["REDIS_PASSWORD"]
        )

        newResponse = newRedis.ping()
        logging.info(
            "successfully connected to redis using credate_redis_instance()")
        newRedis.close()
    except ConnectionError as ce:
        logging.error(ce.strerror())
    try:
        assert newResponse == knownResponse, logging.info(
            "Responses Match. function create_redis_instance() functions")
    except AssertionError as e:
        logging.error(
            "create_redis_instance() function does not connect in expected\
             manor")
        logging.error("Assertion failed:", e)
