"""
角色添加右上角
select code from role;
"""
from utils.constant.constant import Constant


class AddCommonlyTool:
    def __init__(self):
        pass

    def handle(self):
        sql = 'insert into role_permission_relation(gmt_create, gmt_modify, role_code, permission_code) values '

        print(sql)

        with open(Constant.BASE_PATH + 'role.txt') as f:
            for line in f.readlines():
                print('(now(), now(), "' + line[:-1] + '", "releaseTask"),')
                print('(now(), now(), "' + line[:-1] + '", "releaseMatter"),')
                print('(now(), now(), "' + line[:-1] + '", "releaseRepair"),')
        print(';')


if __name__ == '__main__':
    handle = AddCommonlyTool()
    handle.handle()
