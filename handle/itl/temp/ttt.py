base_sql = 'INSERT INTO role_permission_relation(gmt_create, gmt_modify, role_code, permission_code) VALUES (now(), now(), "{role_code}", "{permission_code}");'

with open('hehehheheheheh.txt', 'r') as f:
    for line in f.readlines():
        print(base_sql.format(role_code='后台项目管理员', permission_code=line[:-1]))
