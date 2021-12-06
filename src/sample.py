import logging
import traceback

from common import utils
from setting.Setting import Setting

utils.set_logger()
logger = logging.getLogger(__name__)

setting = Setting("test")
logger.debug("test1")
logger.info("test2")
logger.warn("test3")
logger.error("test4")
logger.critical("test5")

try:
    a = 10 / 0
except Exception as e:
    logger.warn(e.args)
    logger.debug(traceback.format_exc())
