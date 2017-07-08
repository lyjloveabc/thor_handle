"""

"""
from handle.itl.handleFor170716.dbUtil import DbUtil
from handle.itl.handleFor170716.menu.data.roleData import RoleData


class UserRole:
    _BASE_SQL_UPDATE = "UPDATE user_role_relation SET role_code = '{role_code}' WHERE role_code = '{old_role_code}';"
    _BASE_SQL_TRAN = "INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '{user_id}', '前台客服');"
    _BASE_SQL_DEL = "DELETE FROM user_role_relation WHERE role_code IN ('jobAdjustment', 'companyManager', 'energyMeterReader', 'businessExecutive', 'liftWorker');"

    def __init__(self, *args, **kw):
        self.dbUtil = kw['dbUtil']

    def handle(self):
        self._update()
        self._tran()
        self._del()

    def _update(self):
        sql_define = list()
        for row in RoleData.ROLE:
            sql = UserRole._BASE_SQL_UPDATE.format(old_role_code=row['old_code'], role_code=row['code'])
            sql_define.append(sql)

        self.dbUtil.out_sql(sql_define, '')
        self.dbUtil.exe_on_db(sql_define)

    def _tran(self):
        self.dbUtil.out_sql([UserRole._BASE_SQL_DEL], '')
        self.dbUtil.exe_on_db([UserRole._BASE_SQL_DEL])

    def _del(self):
        sql_define = list()

        ids = self.dbUtil.temp()
        for row in ids:
            sql_define.append(UserRole._BASE_SQL_TRAN.format(user_id=row['id']))

        self.dbUtil.out_sql(sql_define, '')
        self.dbUtil.exe_on_db(sql_define)


if __name__ == '__main__':
    handle = UserRole(**{'dbUtil': DbUtil()})
    handle.handle()
