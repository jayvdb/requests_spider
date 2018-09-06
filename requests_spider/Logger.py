import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] - [%(levelname)s] - 【Snake】- [%(message)s]',
    datefmt='%Y/%m/%d %H:%M:%S')

logger = logging.getLogger(__name__)

