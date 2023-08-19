import redis
import os
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Redis functions loaded")


def create_redis_instance(host,
                          port,
                          channel,
                          password):
    try:
        return redis.Redis(
            host=host, port=port, decode_responses=True, password=password)
    except Exception as e:
        logger.error(f"Error creating redis instance: {e}")
        print(e)
        return None


def publish_vote_to_redis(redis_instance, vote):
    try:
        message = {vote}
        redis_instance.publish(os.environ["REDIS_CHANNEL"], message)
        logger.info(f"Published to redis: {message}")
        return message
    except Exception as e:
        logger.error(f"Error publishing to redis: {e}")
        print(e)
        return None
