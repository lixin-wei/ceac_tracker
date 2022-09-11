from refresh_once import refresh_once
from ischedule import run_loop, schedule
from my_logging import get_logger

logger = get_logger(__file__)

if __name__ == "__main__":

    def refresh_once_safe():
        try:
            refresh_once()
        except:
            logger.exception("Refresh failed!")

    schedule(refresh_once_safe, interval=5)
    run_loop()
