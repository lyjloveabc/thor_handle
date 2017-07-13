"""
A
九公生成的角色权限关系
"""
from handle.itl.handleFor170716.dbUtil import DbUtil


class JgRolePermission:
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

        role_permission_relation = self.dbUtil.role_permission_relation()

        for row in role_permission_relation:
            role_code = JgRolePermission._get_role_code(row['role_code'])
            sql = JgRolePermission._BASE_SQL_R.format(role_code=role_code, permission_code=row['permission_code'])
            sql_define.append(sql)

        self.dbUtil.out_sql(sql_define, '')
        self.dbUtil.exe_on_db(sql_define)

    @staticmethod
    def _get_role_code(old_role_code):
        return {'propertyManager': '物业公司管理员', 'xiaoer': '小二'}[old_role_code]


if __name__ == '__main__':
    handle = JgRolePermission(**{'dbUtil': DbUtil()})
    handle.handle()
