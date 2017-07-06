"""
存储sql到特定文件
"""
import os
from datetime import datetime

from utils.constant.constant import Constant
from utils.db.daoUtil import DaoUtils
from utils.db.mysql.mySQLConfig import MySQLConfig


class DbUtil:
    _BASE_PATH = './'
    _DIRECT_EXE_ON_DB = True

    def __init__(self):
        self.dao = DaoUtils(**{'dbType': 'MySQL', 'config': MySQLConfig.localhost()})
        self.time = datetime.now().strftime('%Y%m%d%H%M%S')

        if not os.path.exists(DbUtil._BASE_PATH):
            os.mkdir(DbUtil._BASE_PATH)

    def out_sql(self, data, remark=''):
        with open(DbUtil._BASE_PATH + 'out' + self.time + '.sql', 'a') as f:
            f.write('# ' + remark + Constant.NEW_LINE)
            f.write(Constant.SQL_BEGIN + Constant.NEW_LINE)
            for row in data:
                f.write(row + Constant.NEW_LINE)
            f.write(Constant.SQL_COMMIT + Constant.NEW_LINE)

    def exe_on_db(self, data):
        if DbUtil._DIRECT_EXE_ON_DB:
            for row in data:
                self.dao.dao.execute(row)

    def get_all_role(self):
        return self.dao.get_all('SELECT code FROM role ORDER BY id;')


if __name__ == '__main__':
    handle = DbUtil()
    handle.out_sql(['SELECT * FROM user;', 'SELECT * FROM users;'], '呵呵')
