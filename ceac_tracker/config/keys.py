import json
import os
from ceac_tracker.utils.my_logging import get_logger

logger = get_logger(__file__)
config_root = os.path.dirname(__file__)


def get_keys():
    with open(os.path.join(config_root, "keys.json"), "r") as f:
        return json.loads(f.read())


if __name__ == "__main__":
    keys = get_keys()
    logger.info(keys)
    logger.info(keys["2capture_key"])
