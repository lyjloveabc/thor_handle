"""

"""

__AUTHOR = 'thor'


class AddCommonlyTool(object):
    __BASE_PATH = 'file/'

    def __init__(self):
        self.sql = 'insert into role_permission_relation(gmt_create, gmt_modify, role_code, permission_code) values '

    def handle(self):
        print(self.sql)

        with open(AddCommonlyTool.__BASE_PATH + 'role.txt') as f:
            for line in f.readlines():
                info_array = line[:-1].split(',')
                print('(now(), now(), "' + info_array[3] + '", "releaseTask"),')
                print('(now(), now(), "' + info_array[3] + '", "releaseMatter"),')
                print('(now(), now(), "' + info_array[3] + '", "releaseRepair"),')
        print(';')


if __name__ == '__main__':
    handle = AddCommonlyTool()
    handle.handle()
