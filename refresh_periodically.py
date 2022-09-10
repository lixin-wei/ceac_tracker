from refresh_once import refresh_once
from ischedule import run_loop, schedule

if __name__ == "__main__":
    schedule(refresh_once, interval=1800)
    run_loop()
