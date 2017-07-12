"""
处理新的用户ID
"""
from handle.itl.handleFor170716.dbUtil import DbUtil
from handle.itl.handleFor170716.menu.data.menuData import MenuData


class HandleNewUserId:
    _BASE_SQL_PERMISSION = "INSERT INTO permission " \
                           "(gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) " \
                           "VALUES (now(), now(), '{parent_id}', '{code}', '{name}', '{type}', '{function_url}','{menu_type}', '{icon_url}', '{description}', " \
                           "'{sort_num}', '{checked}', '{menu_kind}');"

    _BASE_SQL_R = 'INSERT INTO role_permission_relation' \
                  '(gmt_create, gmt_modify, role_code, permission_code) ' \
                  'VALUES ' \
                  '(now(), now(), "{role_code}", "{permission_code}");'

    def __init__(self, *args, **kw):
        self.dbUtil = DbUtil()

    def handle(self):
        self._delete_old_data()
        self._create_plus()
        self._create_tool()
        self._create_my()

    def _delete_old_data(self):
        sql_define = ["DELETE FROM permission WHERE type = 'MENU';", "DELETE FROM role_permission_relation;"]
        self.dbUtil.out_sql(sql_define, '删除所有的permission，role_permission_relation数据')
        self.dbUtil.exe_on_db(sql_define)

    def _create_plus(self):
        sql_define_permission = list()
        sql_define_r = list()

        role_codes = self.dbUtil.get_all_role()

        for plus in MenuData.COMMON_PLUS:
            sql_define_permission.append(HandleNewUserId._BASE_SQL_PERMISSION.format(parent_id=0, code=plus['code'], name=plus['name'], type='MENU', function_url='',
                                                                                     menu_type=plus['menu_type'], icon_url='', description=plus['name'],
                                                                                     sort_num=plus['sort_num'], checked='TRUE', menu_kind=plus['menu_kind']))
        for role_code in role_codes:
            for plus in MenuData.COMMON_PLUS:
                sql_define_r.append(HandleNewUserId._BASE_SQL_R.format(role_code=role_code['code'], permission_code=plus['code']))
        self.dbUtil.out_sql(sql_define_permission, '创建管家端右上角+号的菜单')
        self.dbUtil.out_sql(sql_define_r, '创建右上角的+菜单和角色对应的关系')
        self.dbUtil.exe_on_db(sql_define_permission)
        self.dbUtil.exe_on_db(sql_define_r)

    def _create_tool(self):
        sql_define_permission = list()
        sql_define_r = list()

        role_codes = self.dbUtil.get_all_role()

        for tool in MenuData.TOOLS:
            sql_define_permission.append(HandleNewUserId._BASE_SQL_PERMISSION.format(parent_id=0, code=tool['code'], name=tool['name'], type='MENU',
                                                                                     function_url=tool['function_url'] if 'function_url' in tool else '',
                                                                                     menu_type=tool['menu_type'], icon_url=tool['icon_url'],
                                                                                     description=tool['name'], sort_num=tool['sort_num'], checked='TRUE',
                                                                                     menu_kind='HOUSEKEEPER'))
        for role_code in role_codes:
            for plus in MenuData.TOOLS:
                sql_define_r.append(HandleNewUserId._BASE_SQL_R.format(role_code=role_code['code'], permission_code=plus['code']))
        self.dbUtil.out_sql(sql_define_permission, '创建管家端工具入口')
        self.dbUtil.out_sql(sql_define_r, '创建家端工具入口和角色对应的关系')
        self.dbUtil.exe_on_db(sql_define_permission)
        self.dbUtil.exe_on_db(sql_define_r)

    def _create_my(self):
        sql_define_permission = list()
        sql_define_r = list()

        role_codes = self.dbUtil.get_all_role()

        for my in MenuData.MY:
            sql_define_permission.append(HandleNewUserId._BASE_SQL_PERMISSION.format(
                parent_id=0, code=my['code'], name=my['name'], type='MENU',
                function_url='',
                menu_type=my['menu_type'], icon_url=my['icon_url'],
                description=my['name'], sort_num=my['sort_num'], checked='TRUE',
                menu_kind='HOUSEKEEPER_MY_TAB'))
        for role_code in role_codes:
            for plus in MenuData.MY:
                sql_define_r.append(HandleNewUserId._BASE_SQL_R.format(role_code=role_code['code'], permission_code=plus['code']))
        self.dbUtil.out_sql(sql_define_permission, '创建管家端我的TAB里面的菜单')
        self.dbUtil.out_sql(sql_define_r, '创建管家端我的TAB里面的菜单和角色对应的关系')
        self.dbUtil.exe_on_db(sql_define_permission)
        self.dbUtil.exe_on_db(sql_define_r)


if __name__ == '__main__':
    handle = HandleNewUserId()
    handle.handle()