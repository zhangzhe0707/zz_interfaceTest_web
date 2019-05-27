import os
import codecs
import configparser

PROJECT_DIR = os.path.split(os.path.realpath(__file__))[0]
CONFIG_PATH = os.path.join(PROJECT_DIR, 'config', 'config.ini')
RESPORTS_DIR_PATH = os.path.join(PROJECT_DIR, 'reports')
ENCODING = 'UTF-8'


class OperationConfig:
    def __init__(self):
        with open(CONFIG_PATH, encoding=ENCODING) as file_object:
            config_data = file_object.read()

            # 移除文件中的BOM BOM = b'\xef\xbb\xbf'
            if config_data[:3] == codecs.BOM_UTF8:
                config_data = config_data[3:]
                with open(CONFIG_PATH, 'w', encoding=ENCODING) as file_object:
                    file_object.write(config_data)
            self.config_file = configparser.ConfigParser()
            self.config_file.read(CONFIG_PATH, encoding=ENCODING)

    def get_email(self, name):
        """
        获取 email 相关配置的对应值
        :param self:
        :param name:Email配置关键字名称
        :return:
        """
        value = self.config_file.get('EMAIL', name)
        return value

    def get_http(self, name):
        """
        获取http配置
        :param self:
        :param name: HTTP配置关键字名称
        :return:
        """
        value = self.config_file.get('HTTP', name)
        return value

    def get_db(self, name):
        """
        获取数据库配置
        :param self:
        :param name: DB配置关键字名称
        :return:
        """
        value = self.config_file.get('DATABASE', name)
        return value

    def get_mail(self, name):
        """
        获取邮件配置
        :param self:
        :param name: 邮件配置关键字名称
        :return:
        """
        value = self.config_file.get('MAIL', name)
        return value

    def get_db_index(self, name):
        """
        获取db 数据结果字段对应索引号
        :param self:
        :param name:  db表名字段
        :return:
        """
        value = int(self.config_file.get('db_index', name))
        return value

    def get_report(self, name):
        """
        获取Excel字段对应列号
        :param self:
        :param name: Excel 字段列名
        :return:
        """
        value = self.config_file.get('REPORT', name)
        return value

    def set_report(self, name, value):
        # 修改REPOST 配置里面的值
        self.config_file.set("REPORT", name, value)  # 写入中文

        self.config_file.write(open(CONFIG_PATH, "r+", encoding=ENCODING))  #

    def get_env(self, name):
        """
        获取env配置
        :param self:
        :param name:
        :return:
        """
        value = self.config_file.get('ENV', name)
        return value

    def set_env(self, name, value):
        # 修改env配置的值
        self.config_file.set("ENV", name, value)

        self.config_file.write(open(CONFIG_PATH, "r+", encoding=ENCODING))  #


if __name__ == "__main__":
    from datetime import datetime

    print(PROJECT_DIR)
    print(CONFIG_PATH)
    print(RESPORTS_DIR_PATH)
    OC = OperationConfig()
    print(OC.get_http('baseurl'))
    log_path = os.path.join(RESPORTS_DIR_PATH, str(datetime.now().strftime("%Y%m%d%H%M%S")))
    print(log_path)
    OC.set_report('path', "jjjj")
