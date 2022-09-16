# Quick Start

## Install Package

```bash
pip instsall -e ./ -v
```

## Init Database

```bash
python ceac_tracker/db/sqlite_store.py
```

Insert application_id to database manually.

## Configure Third-Party Service Keys

```bash
cp ceac_tracker/config/keys_template.json keys.json
```

Then edit `keys.json`

## Refresh Once

```bash
python ceac_tracker/refresh_once.py
```

## Run Periodically

```bash
# The number indicates interval in seconds
python ceac_tracker/refresh_periodically.py 3600

# Run in background. `-u` means disable output buffer
# or nohup.out will have no log.
nohup python -u ceac_tracker/refresh_periodically.py 3600&
```

# For Developers: How to Replace Third-Party Services

I use [2captcha](https://2captcha.com/) to resolve captcha.

And use [DingTalk Robot](https://open.dingtalk.com/document/robots/custom-robot-access) for notification.

You probably need to replace them if you don't want to use these two service.

To replace captcha resolving service, you need to implement another `resolve_captcha(image_base64)` function similar to what in `two_captcha_resolve.py`,
and replace all `resolve_captcha` to your own function.

```python
def resolve_captcha(image_base64: str) -> str:
    pass
```

To replace notification service, try to replace `ding_talk_notice(msg)` to your own function.

Sorry for the unplugable code, but it's only for my own use now. Welcome for pull requests to make it better.
