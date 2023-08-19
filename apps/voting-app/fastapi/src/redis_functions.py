import redis
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Redis functions loaded")


def create_redis_instance(host, port, channel, password, ):
    try:
        return redis.Redis(
            host=host, port=port, decode_responses=True, password=password)
    except Exception as e:
        logger.error(f"Error creating redis instance: {e}")
        print(e)
        return None


def publish_to_redis(redis_instance, user_hash, vote):
    try:
        message = "{" + f"'{user_hash}': '{vote}'" + "}"
        reddis_instance.publish(os.environ["REDIS_CHANNEL"], message)
        logger.info(f"Published to redis: {message}")
        return True
    except Exception as e:
        logger.error(f"Error publishing to redis: {e}")
        print(e)
        return False
