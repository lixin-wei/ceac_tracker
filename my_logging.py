import logging

logging.basicConfig(format="%(asctime)s %(levelname)s %(filename)s:%(lineno)d | %(message)s", level=logging.INFO)


def get_logger(name):
    return logging.getLogger(name)
