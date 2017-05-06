"""
密码
"""


class SkyPwd(object):
    __BASE_PATH = 'file/'

    def __init__(self):
        self.base_sql = 'update user set password = "{password}" where mobile = {mobile};'

    def handle(self):
        mobile_pwd = list()
        with open(SkyPwd.__BASE_PATH + 'admin_user_zone_pwd.txt', 'r') as f:
            for line in f.readlines():
                line_split = line[:-1].split(',')
                item = {
                    'mobile': line_split[0],
                    'pwd': line_split[1]
                }
                mobile_pwd.append(item)

        user_exist_mobile = set()
        with open(SkyPwd.__BASE_PATH + 'user已经存在的mobile.txt', 'r') as f:
            for line in f.readlines():
                user_exist_mobile.add(line[:-1])

        with open(SkyPwd.__BASE_PATH + 'pwd_out.sql', 'w') as f:
            f.write('BEGIN;\n')
            size = len(mobile_pwd)
            for index in range(size):
                if mobile_pwd[index]['mobile'] in user_exist_mobile:
                    sql = self.base_sql.format(password=mobile_pwd[index]['pwd'], mobile=mobile_pwd[index]['mobile'])
                    f.write(sql + '\n')
                else:
                    print(mobile_pwd[index]['mobile'])

            f.write('COMMIT;\n')


if __name__ == '__main__':
    handle = SkyPwd()
    handle.handle()
