"""
通过老的管家端员工信息
把头像
映射到新的用户上面
"""

__AUTHOR = 'thor'


class AvatarMapper(object):
    __BASE_PATH = 'file/'

    def __init__(self):
        pass

    def handle(self):
        old = dict()
        with open(AvatarMapper.__BASE_PATH + 'admin_employee.txt', 'r') as f:
            for line in f.readlines():
                temp = line[:-1].split(',')
                old[temp[0]] = temp[1]

        print('BEGIN;')
        with open(AvatarMapper.__BASE_PATH + 'user.txt', 'r') as f:
            for line in f.readlines():
                temp = line[:-1].split(',')
                if temp[1] in old:
                    print('update user set avatar_url = "' + old[temp[1]] + '" where id = ' + temp[0] + ';')
        print('COMMIT;')


if __name__ == '__main__':
    handle = AvatarMapper()
    handle.handle()
