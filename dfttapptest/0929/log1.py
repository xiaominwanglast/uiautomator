#coding:utf-8
import logging
import sys

logger = logging.getLogger(__name__)
filter = logging.Filter(__name__)
formatter = logging.Formatter("%(asctime)s|%(name)-12s|%(message)s", "%F %T")

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.addFilter(filter)
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

logger.setLevel(logging.DEBUG)
logger.addFilter(filter)
logger.addHandler(stream_handler)

if __name__ == "__main__":
    logger.info("info")