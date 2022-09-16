import requests
import time
from ceac_tracker.config.keys import get_keys
from ceac_tracker.utils.my_logging import get_logger

logger = get_logger(__file__)


def resolve_captcha(image_base64):
    # logger.info(image_base64)
    two_capture_key = get_keys()["2capture_key"]
    res = requests.post(
        "http://2captcha.com/in.php",
        data={
            "method": "base64",
            "key": two_capture_key,
            "body": image_base64,
            "json": 1,
        },
    )
    logger.info(res.json())
    id = res.json()["request"]
    text = "CAPCHA_NOT_READY"
    while text == "CAPCHA_NOT_READY":
        time.sleep(1)
        res2 = requests.get(
            "http://2captcha.com/res.php",
            params={
                "key": two_capture_key,
                "action": "get",
                "id": id,
                "json": 1,
            },
        )
        logger.info(res2.json())
        text = res2.json()["request"]
    logger.info(f"Captcha resolved! result={text}")
    return text
