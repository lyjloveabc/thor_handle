class Nos:
    def __init__(self):
        pass

    def handle(self):
        pass


if __name__ == '__main__':
    account = list()

    with open('file/needOpenSky.txt', 'r') as f:
        for line in f.readlines():
            account.append("'" + line[:-1] + "'")
    sql = 'SELECT id FROM user WHERE account IN ({accounts});'
    print(sql.format(accounts=','.join(account)))

    sql_insert = 'INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), {user_id}, "天眼人员");'

    with open('file/temp.txt', 'r') as f:
        for line in f.readlines():
            print(sql_insert.format(user_id=line[:-1]))
