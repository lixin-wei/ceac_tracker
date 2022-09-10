import json


def get_keys():
    with open("keys.json", "r") as f:
        return json.loads(f.read())


if __name__ == "__main__":
    keys = get_keys()
    print(keys)
    print(keys["2capture_key"])
