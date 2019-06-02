import os
import logging
import operationConfig

LOCAL_READ_CONFIG = operationConfig.OperationConfig()
ENCODING = 'UTF-8'


class Log:
    def __init__(self):
        log_path = LOCAL_READ_CONFIG.get_report('path')

        # 定义 logger 实例
        self.logger = logging.getLogger()

        # 定义日志级别
        self.logger.setLevel(logging.INFO)

        # 定义日志路径默认
        defaulthandler = logging.FileHandler(os.path.join(log_path, "output.log"),
                                             encoding=ENCODING)

        # 定义默认日志的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        defaulthandler.setFormatter(formatter)

        # 给logger实例添加handler
        self.logger.addHandler(defaulthandler)

    def get_logger(self):
        """
        获取log 日志
        :return:
        """
        return self.logger

    def add_start_line(self, case_no):
        """
        写入开启记录日志标识行
        :param case_no:
        :return:
        """
        self.logger.info("---------CaseName:{0} START--------".format(case_no))

    def add_end_line(self, case_no):
        """
        写入结束记录日志标识行
        :param case_no:
        :return:
        """
        self.logger.info("---------CaseName:{0} END--------".format(case_no))


if __name__ =="__main__":
    lg = Log()
    log_object = lg.get_logger()
    log_object.error("错误信息")
    log_object.info("info 日志信息")