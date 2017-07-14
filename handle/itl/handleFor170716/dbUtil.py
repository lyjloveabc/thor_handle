"""
存储sql到特定文件
"""
import os
from datetime import datetime

from utils.constant.constant import Constant
from utils.db.daoUtil import DaoUtils
from utils.db.mysql.mySQLConfig import MySQLConfig


class DbUtil:
    _BASE_PATH = './sql/'
    _DIRECT_EXE_ON_DB = False

    def __init__(self):
        self.dao = DaoUtils(**{'dbType': 'MySQL', 'config': MySQLConfig.stable_sky()})
        self.time = datetime.now().strftime('%Y%m%d%H%M%S')

        self.users = self.get_all_user()
        self.admin_emp = self.get_all_admin_emp()

        self.where = ''

        if not os.path.exists(DbUtil._BASE_PATH):
            os.mkdir(DbUtil._BASE_PATH)

    def out_sql(self, data, remark=''):
        with open(DbUtil._BASE_PATH + 'out' + self.time + '.sql', 'a') as f:
            f.write('# ' + remark + Constant.NEW_LINE)
            # f.write(Constant.SQL_BEGIN + Constant.NEW_LINE)
            for row in data:
                f.write(row + Constant.NEW_LINE)
            # f.write(Constant.SQL_COMMIT + Constant.NEW_LINE)
            f.write(Constant.NEW_LINE)

    def exe_on_db(self, data):
        if DbUtil._DIRECT_EXE_ON_DB:
            for row in data:
                self.dao.dao.execute(row)

    def get_user_id(self, admin_id):
        for emp in self.admin_emp:
            if emp['id'] == admin_id:
                for row in self.users:
                    if emp['mobile'] in row['account']:
                        return row['id']
        return 0

    def get_user(self, admin_id):
        for emp in self.admin_emp:
            if emp['id'] == admin_id:
                for row in self.users:
                    if emp['mobile'] in row['account']:
                        return {'id': row['id'], 'name': row['name']}
        return {'id': 0, 'name': ''}

    def get_all_role(self):
        return self.dao.get_all('SELECT code FROM role ORDER BY id;')

    def get_all_user(self):
        return self.dao.get_all('SELECT id, account, name FROM user ORDER BY id;')

    def get_all_admin_emp(self):
        return self.dao.get_all('SELECT id, mobile FROM admin_employee ORDER BY id;')

    def get_all_subscription_enter(self):
        return self.dao.get_all('SELECT id, admin_employee_id FROM subscription_enter ' + self.where + ';')

    def get_all_repair(self):
        return self.dao.get_all('SELECT id, guid, employee_id FROM task;')

    def get_all_task_map(self):
        return self.dao.get_all('SELECT id, uid FROM task_map;')

    def get_all_appraisal(self):
        return self.dao.get_all('SELECT id, eid FROM appraisal;')

    def get_all_appraisal_emp(self):
        return self.dao.get_all('SELECT id, eid FROM appraisal_emp;')

    def get_all_appraisal_progress(self):
        return self.dao.get_all('SELECT id, eid FROM appraisal_progress;')

    def get_all_appraisal_adjust(self):
        return self.dao.get_all('SELECT id, eid FROM appraisal_adjust;')

    def get_all_appraisal_assignee(self):
        return self.dao.get_all('SELECT id, eid FROM appraisal_assignee;')

    def get_all_summary_plan(self):
        return self.dao.get_all('SELECT id, employee_id FROM summary_plan;')

    def get_all_bug_report(self):
        return self.dao.get_all('SELECT id, uid FROM bug_report;')

    def get_all_chat(self):
        return self.dao.get_all('SELECT id, reply_id FROM chat;')

    def get_about_appraisal(self):
        return [
            {'table': 'appraisal', 'data': self.get_all_appraisal()},
            {'table': 'appraisal_emp', 'data': self.get_all_appraisal_emp()},
            {'table': 'appraisal_progress', 'data': self.get_all_appraisal_progress()},
            {'table': 'appraisal_adjust', 'data': self.get_all_appraisal_adjust()},
            {'table': 'appraisal_assignee', 'data': self.get_all_appraisal_assignee()},
        ]

    # START TEMP
    def temp(self):
        return self.dao.get_all('SELECT id FROM user_role_relation WHERE role_code = \'customerService\';')

    def role_permission_relation(self):
        return self.dao.get_all('SELECT role_code, permission_code FROM role_permission_relation WHERE role_code IN (\'propertyManager\', \'xiaoer\');')

    def get_all_zones(self):
        return self.dao.get_all('SELECT id FROM user_role_relation WHERE role_code = \'customerService\';')

    def get_wh_role_per_r(self):
        return self.dao.get_all('SELECT role_code, permission_code FROM role_permission_relation WHERE id >= 3432 AND id <= 4029;')


if __name__ == '__main__':
    handle = DbUtil()
    handle.out_sql(['SELECT * FROM user;', 'SELECT * FROM users;'], '呵呵')
