import json
from my_logging import get_logger

logger = get_logger(__file__)


def get_keys():
    with open("keys.json", "r") as f:
        return json.loads(f.read())


if __name__ == "__main__":
    keys = get_keys()
    logger.info(keys)
    logger.info(keys["2capture_key"])
