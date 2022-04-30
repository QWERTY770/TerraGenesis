import logging
import os
import time
from os.path import join, abspath

t = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(join(join(abspath(join(os.getcwd(), "..")), "logs"), f"{t}.log"),
                              mode="w")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
