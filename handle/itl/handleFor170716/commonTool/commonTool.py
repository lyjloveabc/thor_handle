"""
上线的工具入口整理
"""
import os


class CommonTool:
    BASE_PATH = 'file/'

    def __init__(self):
        self.base_sql = 'insert into permission' \
                        '(gmt_create, gmt_modify, parent_id, code, name, type, function_url,' \
                        'menu_type, icon_url, description, sort_num, checked, menu_kind) ' \
                        'values ' \
                        '(now(), now(), "0", "{code}", "{name}", "MENU", "{function_url}",' \
                        '"{menu_type}", "{icon_url}", "{description}", "{sort_num}", "TRUE", "COMMONLY_TOOL");'

        if not os.path.exists(CommonTool.BASE_PATH):
            os.mkdir(CommonTool.BASE_PATH)

    def handle(self):
        data_source = [
            'housekeeper_dataCenter 数据中心 10001 http://oda3qkbe9.bkt.clouddn.com/icon-shuju@3x.png',
            'housekeeper_dataCenter 数据中心 10001 http://oda3qkbe9.bkt.clouddn.com/icon-shuju@3x.png',
            'housekeeper_dataCenter 数据中心 10001 http://oda3qkbe9.bkt.clouddn.com/icon-shuju@3x.png',
        ]

        with open(CommonTool.BASE_PATH + 'commonTool_out.sql', 'w') as f:
            f.write('BEGIN;\n')

            index = 1
            for row in data_source:
                function_url = ''
                if len(row) == 5:
                    function_url = row[4]
                sql = self.base_sql.format(code=row[0], name=row[1], function_url=function_url,
                                           menu_type=row[2], icon_url=row[3], description=row[1], sort_num=index)
                f.write(sql + '\n')
                index += 1

            f.write('COMMIT;\n')


if __name__ == '__main__':
    handle = CommonTool()
    handle.handle()
