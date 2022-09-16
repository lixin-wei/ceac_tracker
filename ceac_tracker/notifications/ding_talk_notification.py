import requests
from ceac_tracker.config.keys import get_keys

def send_notification(message, recevier):
    ding_talk_key = get_keys()["ding_talk_key"]
    requests.post(
        f"https://oapi.dingtalk.com/robot/send?access_token={ding_talk_key}",
        json={"msgtype": "text", "text": {"content": f"Notice: recevier={recevier}, msg={message}"}},
    )

if __name__ == "__main__":
    send_notification("Hello!")