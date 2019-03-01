import logging
import os
import datetime

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
#控制台输出日志
# console = logging.StreamHandler()
# formatter0 = logging.Formatter("%(asctime)s %(filename)s %(funcName)s %(lineno)d %(levelname)s ---->%(message)s")
# console.setFormatter(formatter0)
# logger.addHandler(console)
logger.debug("info")
#文件输出日志
base_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(base_dir,"logs")
log_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
log_name = os.path.join(log_dir,log_file)
file_handle = logging.FileHandler(filename=log_name,mode="a",encoding="utf-8")
formatter = logging.Formatter("%(asctime)s %(filename)s %(funcName)s %(lineno)d %(levelname)s ---->%(message)s")
file_handle.setFormatter(formatter)
logger.addHandler(file_handle)

logger.info("test")
logger.removeHandler(file_handle)
file_handle.close()