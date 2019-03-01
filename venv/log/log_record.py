import logging
import datetime
import os

# def decorator(func):
#     def log_test(self):
#         logger = func(self)
#         self.logger.removeHandler(self.file_handle)
#         self.file_handle.close()
#         print(222)
#         return logger
#     return log_test

class LogRecord:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        #文件输出日志
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir,"logs")
        log_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
        log_name = os.path.join(log_dir,log_file)
        self.file_handle = logging.FileHandler(filename=log_name,mode="a",encoding="utf-8")
        self.file_handle.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s %(filename)s %(funcName)s %(lineno)d %(levelname)s ---->%(message)s")
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)

    #@decorator
    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()


if __name__ == "__main__":
    r = LogRecord()
    print(r)
    log = r.get_log()
    print(log)
    log.debug()
    # LogRecord.get_log()