"""
所有的角色都有属性
"""
from handle.itl.handleFor170716.dbUtil import DbUtil
from handle.itl.handleFor170716.menu.data.roleData import RoleData


class RoleAttribute:
    _BASE_SQL_PERMISSION = "INSERT INTO role_attribute " \
                           "(id, gmt_create, gmt_modify, role_code, can_be_bonus_points, can_be_complaint_praise, can_change_zone, can_be_repair_task) " \
                           "VALUES ('{id}' ,now(), now(), '{role_code}', '1', '1', '1', '1');"

    def __init__(self, *args, **kw):
        self.dbUtil = kw['dbUtil']

    def handle(self):
        self._add_role()

    def _add_role(self):
        sql_define = list()

        index = 21

        for row in RoleData.ROLE:
            sql = RoleAttribute._BASE_SQL_PERMISSION.format(id=index, role_code=row['code'])
            sql_define.append(sql)
            index += 1

        for row in RoleData.ROLE_ADD:
            sql = RoleAttribute._BASE_SQL_PERMISSION.format(id=index, role_code=row['code'])
            sql_define.append(sql)
            index += 1
        self.dbUtil.out_sql(sql_define, '角色属性表新增所有的角色对应的属性')
        self.dbUtil.exe_on_db(sql_define)


if __name__ == '__main__':
    handle = RoleAttribute(**{'dbUtil': DbUtil()})
    handle.handle()
