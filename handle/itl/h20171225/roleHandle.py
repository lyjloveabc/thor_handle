sql = 'INSERT INTO role_permission_relation (id, gmt_create, gmt_modify, role_code, permission_code) VALUES ({id}, now(), now(), "{code}", "commonTool_face_pay");'

with open('role.txt', 'r') as f:
    index = 3543
    for row in f.readlines():
        row = row.replace('\n', '')
        print(sql.format(id=index, code=row))
        index += 1
