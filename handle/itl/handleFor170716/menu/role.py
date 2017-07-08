"""
处理菜单
"""
from handle.itl.handleFor170716.dbUtil import DbUtil
from handle.itl.handleFor170716.menu.data.roleData import RoleData


class Role:
    _BASE_SQL_PERMISSION = "INSERT INTO role " \
                           "(gmt_create, gmt_modify, code, name, description) " \
                           "VALUES (now(), now(), '{code}', '{name}', '{description}');"

    def __init__(self, *args, **kw):
        self.dbUtil = kw['dbUtil']

    def handle(self):
        self._add_role()

    def _add_role(self):
        sql_define = list()
        for row in RoleData.ROLE:
            sql = Role._BASE_SQL_PERMISSION.format(code=row['code'], name=row['code'], description=row['code'])
            sql_define.append(sql)
        for row in RoleData.ROLE_ADD:
            sql = Role._BASE_SQL_PERMISSION.format(code=row['code'], name=row['code'], description=row['code'])
            sql_define.append(sql)
        self.dbUtil.out_sql(sql_define, '新增所有的角色')
        self.dbUtil.exe_on_db(sql_define)


if __name__ == '__main__':
    handle = Role(**{'dbUtil': DbUtil()})
    handle.handle()
