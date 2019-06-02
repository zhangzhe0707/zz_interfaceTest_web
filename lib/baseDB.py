import pymysql, sqlite3, os
import operationConfig as getConfig
from lib.log import Log

localsGetConfig = getConfig.OperationConfig()


class BaseDB:
    """
    框架操作Mysql/sqlite3的功能封装
    """

    def __init__(self):
        log = Log()
        self.log = log.get_logger()
        self.db_type = localsGetConfig.get_db('db_type')
        if self.db_type == 'mysql':
            self.host = localsGetConfig.get_db('host')
            self.username = localsGetConfig.get_db('username')
            self.password = localsGetConfig.get_db('password')
            self.port = localsGetConfig.get_db('port')
            self.database = localsGetConfig.get_db('database')
            self.config = {
                'host': self.host,
                'user': self.username,
                'password': self.password,
                'port': int(self.port),
                'db': self.database,
                'charset': 'utf8'
            }
        elif self.db_type == 'sqlite3':
            self.db_path = os.path.join(getConfig.PROJECT_DIR, localsGetConfig.get_db('db_path'))
        else:
            self.log.error('数据库类型错误！')

        self.db = None
        self.cursor = None

    def connectDb(self):
        """
        连接数据库
        :param self:
        :return:
        """

        try:
            if self.db_type == 'sqlite3':
                self.db = sqlite3.connect(self.db_path)
                self.cursor = self.db.cursor()
            elif self.db_type == 'mysql':
                self.db = pymysql.connect(**self.config)
                self.cursor = self.db.cursor()
            else:
                self.log.error('数据库类型错误！')
            self.log.info('数据库连接成功!')
        except ConnectionError as ex:
            self.log.error(str(ex))

    def excuteSql(self, sql):
        """
        执行 SQL命令
        :param sql:
        :param params:
        :return:
        """
        self.connectDb()
        self.cursor.execute(sql)
        self.db.commit()
        self.log.info('执行SQL命令为:{0}'.format(sql))
        return self.cursor

    def get_all_data(self, sql):
        """
        获取执行 SQL所有结果数据
        :param cursor:
        :return:
        """
        result = self.excuteSql(sql)
        data = result.fetchall()
        self.log.info('执行数据库查询的结果所有数据:{0}'.format(data))
        self.closeDb()
        return data

    def get_one_data(self, sql):
        """
        获取执行 SQL结果的首行数据
        :param cursor:
        :return:
        """
        result = self.excuteSql(sql)
        data = result.fetchone()
        self.log.info('执行数据库查询的结果单行数据:{0}'.format(data))
        self.closeDb()
        return data

    def get_row_data(self, sql, rows):
        """
        获取执行 SQL结果的指定前n行数据
        :param cursor:
        :param rows:返回指定数据的行数
        :return:
        """
        result = self.excuteSql(sql)
        data = result.fetchmany(rows)
        self.log.info('执行数据库查询的结果指定前{0}行数据:{1}'.format(rows, data))
        self.closeDb()
        return data

    def closeDb(self):
        """
        关闭数据库连接
        :return:
        """
        self.cursor.close()
        self.db.close()
        self.log.info('数据库连接关闭!')


if __name__ == "__main__":
    db = BaseDB()
    print(db.connectDb())
    print(db.get_all_data("select * from WebServer_testcase"))