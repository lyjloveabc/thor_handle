"""
韦护生成的角色权限关系
"""
from handle.itl.handleFor170716.dbUtil import DbUtil


class WhRolePermission:
    _BASE_SQL_R = 'INSERT INTO role_permission_relation' \
                  '(gmt_create, gmt_modify, role_code, permission_code) ' \
                  'VALUES ' \
                  '(now(), now(), "{role_code}", "{permission_code}");'

    def __init__(self, *args, **kw):
        self.dbUtil = kw['dbUtil']

    def handle(self):
        self._add()

    def _add(self):
        sql_define = list()

        role_permission_relation = self.dbUtil.get_wh_role_per_r()

        for row in role_permission_relation:
            sql = WhRolePermission._BASE_SQL_R.format(role_code=row['role_code'], permission_code=row['permission_code'])
            sql_define.append(sql)

        self.dbUtil.out_sql(sql_define, '')
        self.dbUtil.exe_on_db(sql_define)


if __name__ == '__main__':
    handle = WhRolePermission(**{'dbUtil': DbUtil()})
    handle.handle()
