"""
通过老的管家端员工信息
把密码
映射到新的用户上面
"""

__AUTHOR = 'thor'


class PasswordMapper:
    __BASE_PATH = 'file/'

    def __init__(self):
        pass

    @staticmethod
    def handle():
        old = dict()
        with open(PasswordMapper.__BASE_PATH + 'oldUser.txt', 'r') as f:
            for line in f.readlines():
                temp = line[:-1].split(';')
                old[temp[8]] = temp[11]

        print('BEGIN;')
        with open(PasswordMapper.__BASE_PATH + 'newUser.txt', 'r') as f:
            for line in f.readlines():
                temp = line[:-1].split(',')
                if temp[1] in old:
                    print('update user set password = "' + old[temp[1]] + '" where id = ' + temp[0] + ';')
        print('COMMIT;')


if __name__ == '__main__':
    handle = PasswordMapper()
    handle.handle()
