"""
上线的工具入口整理
"""
import os


class HousekeeperMenu:
    BASE_PATH = 'file/'

    def __init__(self):
        self.base_sql = 'insert into permission' \
                        '(gmt_create, gmt_modify, parent_id, code, name, type, function_url,' \
                        'menu_type, icon_url, description, sort_num, checked, menu_kind) ' \
                        'values ' \
                        '(now(), now(), "0", "{code}", "{name}", "MENU", "{function_url}",' \
                        '"{menu_type}", "{icon_url}", "{description}", "{sort_num}", "TRUE", "HOUSEKEEPER");'

        if not os.path.exists(HousekeeperMenu.BASE_PATH):
            os.mkdir(HousekeeperMenu.BASE_PATH)

    def handle(self):
        data_source = list()

        with open(HousekeeperMenu.BASE_PATH + 'toolMenu.txt', 'r') as f:
            for line in f.readlines():
                line_split = line[:-1].split(' ')
                data_source.append(line_split)

        with open(HousekeeperMenu.BASE_PATH + 'housekeeperMenu_out.sql', 'w') as f:
            f.write('BEGIN;\n')

            index = 1000
            for row in data_source:
                function_url = ''
                if len(row) == 5:
                    function_url = row[4]
                sql = self.base_sql.format(code=row[0], name=row[1], function_url=function_url,
                                           menu_type=row[2], icon_url=row[3], description=row[1], sort_num=index)
                f.write(sql + '\n')
                index -= 1
                print('insert into role_permission_relation(gmt_create, gmt_modify, permission_code, role_code) '
                      'values (now(), now(), "' + row[0] + '", "firstPermissionSystemAdmin");')

            f.write('COMMIT;\n')


if __name__ == '__main__':
    handle = HousekeeperMenu()
    handle.handle()
