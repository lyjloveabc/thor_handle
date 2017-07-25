class RolePermission:
    def __init__(self):
        pass

    def handle(self):
        with open('后台项目管理员.txt', 'r') as f:
            for row in f.readlines():
                row_split = row[:-1].split(',')

                print('INSERT INTO role_permission_relation(gmt_create, gmt_modify, role_code, permission_code) '
                      + 'VALUES (now(), now(), "' + row_split[0] + '", "' + row_split[2] + '");')


if __name__ == '__main__':
    obj = RolePermission()
    obj.handle()
