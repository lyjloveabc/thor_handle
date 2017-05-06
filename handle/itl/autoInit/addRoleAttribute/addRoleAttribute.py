"""
添加属性
"""

__AUTHOR = 'thor'


class AddCommonlyTool(object):
    __BASE_PATH = 'file/'

    def __init__(self):
        self.base_sql = "INSERT INTO `role_attribute`(gmt_create, gmt_modify, role_code, can_be_bonus_points)" \
                        "VALUES (now(), now(), '{role}', '1');"

    def handle(self):
        print('BEGIN;')

        with open(AddCommonlyTool.__BASE_PATH + 'role.txt') as f:
            for line in f.readlines():
                info_array = line[:-1].split(' ')
                for item in info_array:
                    print(self.base_sql.format(role=item))
        print('COMMIT;')


if __name__ == '__main__':
    handle = AddCommonlyTool()
    handle.handle()

