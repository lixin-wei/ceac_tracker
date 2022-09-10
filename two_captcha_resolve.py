import requests
import time
from keys import get_keys


def resolve_captcha(image_base64):
    # print(image_base64)
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
    print(res.json())
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
        print(res2.json())
        text = res2.json()["request"]
    print(f"Captcha resolved! result={text}")
    return text
