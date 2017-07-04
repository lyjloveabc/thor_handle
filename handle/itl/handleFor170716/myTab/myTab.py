"""
上线的工具入口整理
"""
import os

from utils.db.daoUtil import DaoUtils
from utils.db.mysql.mySQLConfig import MySQLConfig


class CommonTool:
    BASE_PATH = 'file/'

    def __init__(self):
        self.dao = DaoUtils(**{'dbType': 'MySQL', 'config': MySQLConfig.inner()})

        self.base_sql = 'insert into permission' \
                        '(gmt_create, gmt_modify, parent_id, code, name, type, function_url,' \
                        'menu_type, icon_url, description, sort_num, checked, menu_kind) ' \
                        'values ' \
                        '(now(), now(), "0", "{code}", "{name}", "MENU", "{function_url}",' \
                        '"{menu_type}", "{icon_url}", "{description}", "{sort_num}", "TRUE", "{menu_kind}");'

        self.r_base_sql = 'insert into role_permission_relation' \
                          '(gmt_create, gmt_modify, role_code, permission_code) ' \
                          'values ' \
                          '(now(), now(), "{role_code}", "{permission_code}");'

        self.common_tools = [
            {'code': 'commonTool_releaseTask', 'name': '发布任务', 'menu_type': '1', 'sort_num': '1', 'menu_kind': 'COMMONLY_TOOL'},
            {'code': 'commonTool_releaseMatter', 'name': '发布报事', 'menu_type': '2', 'sort_num': '2', 'menu_kind': 'COMMONLY_TOOL'},
            {'code': 'commonTool_releaseRepair', 'name': '发布报修', 'menu_type': '3', 'sort_num': '4', 'menu_kind': 'COMMONLY_TOOL'}
        ]

        if not os.path.exists(CommonTool.BASE_PATH):
            os.mkdir(CommonTool.BASE_PATH)

    def handle(self):
        self.create_common_tool()
        self.create_role_permission_r()

    def create_common_tool(self):
        with open(CommonTool.BASE_PATH + 'commonTool_out.sql', 'a') as f:
            f.write('BEGIN;\n')
            for common_tool in self.common_tools:
                sql = self.base_sql.format(code=common_tool['code'], name=common_tool['name'], function_url='', menu_type=common_tool['menu_type'],
                                           icon_url='', description=common_tool['name'], sort_num=common_tool['sort_num'], menu_kind=common_tool['menu_kind'])
                f.write(sql + '\n')
            f.write('COMMIT;\n')

    def create_role_permission_r(self):
        role_codes = self.dao.get_all('select code from role order by id;')

        with open(CommonTool.BASE_PATH + 'commonTool_out.sql', 'a') as f:
            f.write('BEGIN;\n')

            for role_code in role_codes:
                for common_tool in self.common_tools:
                    sql = self.r_base_sql.format(role_code=role_code['code'], permission_code=common_tool['code'])
                    f.write(sql + '\n')

            f.write('COMMIT;\n')


if __name__ == '__main__':
    handle = CommonTool()
    handle.handle()
