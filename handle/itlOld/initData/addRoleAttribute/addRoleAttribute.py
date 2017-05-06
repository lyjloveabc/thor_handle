"""
添加属性
"""

__AUTHOR = 'thor'


class AddCommonlyTool(object):
    __BASE_PATH = 'file/'

    def __init__(self):
        self.base_sql = "INSERT INTO `role_attribute` VALUES ('{id}', now(), now(), '{role}', '1');"

    def handle(self):
        print('BEGIN;')

        with open(AddCommonlyTool.__BASE_PATH + 'role.txt') as f:
            index = 2
            for line in f.readlines():
                info_array = line[:-1].split(',')
                print(self.base_sql.format(id=index, role=info_array[3]))
                index += 1
        print('COMMIT;')


if __name__ == '__main__':
    handle = AddCommonlyTool()
    handle.handle()

    # BEGIN;
    # INSERT INTO `role_attribute` VALUES ('1', '2017-03-07 21:39:33', '2017-03-07 21:39:35', 'fristPermissionSystemAdmin', '1');
    # COMMIT;
