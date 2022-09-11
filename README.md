# Quick Start

## Init Database

```bash
python sqlite_store.py
```

Insert application_id to database manually.

## Configure Keys

```bash
cp keys_template.json keys.json
```

Then edit `keys.json`

## Refresh Once

```bash
python refresh_once.py
```

## Run Periodically

```bash
# The number indicates interval in seconds
python refresh_periodically.py 3600

# Run in background. `-u` means disable output buffer
# or nohup.out will have no log.
nohup python -u refresh_periodically.py 3600&
```
