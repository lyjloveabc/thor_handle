import hashlib

from utils.file.excel.readUtil import ReadUtil


class Account:
    _BASE_PATH = 'file/'
    _INSERT_USER = 'INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES ' \
                   '(now(), now(), "{account}", "{password}", "{name}", "{nickname}", (SELECT id FROM itl_company WHERE company_name = "{company_name}"),' \
                   '"{zone_id}", "{zone_ids}");'

    _INSERT_USER_2222 = 'INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES ' \
                        '(now(), now(), "{account}", "{password}", "{name}", "{nickname}", (SELECT id FROM itl_company WHERE company_name = "{company_name}"),' \
                        '(SELECT id FROM zones WHERE name = "{zone_name}"), (SELECT id FROM zones WHERE name = "{zone_name}"));'

    _UPDATE_COMPANY = 'UPDATE itl_company SET manager_id = (SELECT id FROM user WHERE account = "{account}") WHERE company_name = "{company_name}";'

    _UPDATE_ZONE = 'UPDATE zones SET manager_id = (SELECT id FROM user WHERE account = "{account}") WHERE name = "{zone_name}";'

    _INSERT_CATEGORY = 'INSERT INTO itl_zone_category(gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name) VALUES ' \
                       '(now(), now(), (SELECT id FROM zones WHERE name = "{zone_name}"), 11, "项目部");'

    _INSERT_R = 'INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES ' \
                '(now(), now(), (SELECT id FROM user WHERE account = "{account}"), "{role_code}");'

    def handle(self):
        print('SET SQL_SAFE_UPDATES = 0;')
        print('START TRANSACTION;')
        wy = ReadUtil.read_file(Account._BASE_PATH + '物业后台账号-物业公司管理员.xlsx', {'company': 0, 'account': 2, 'pwd': 3})
        for row in wy:
            name = row['company'] + '-管理员'
            print(Account._INSERT_USER.format(account=row['account'], password=hashlib.md5(row['pwd'].encode('utf-8')).hexdigest(),
                                              name=name, nickname=name, company_name=row['company'], zone_id='', zone_ids=''))
            print(Account._UPDATE_COMPANY.format(account=row['account'], company_name=row['company']))
            print(Account._INSERT_R.format(account=row['account'], role_code='物业公司管理员'))

        print()
        print()
        print()

        xm = ReadUtil.read_file(Account._BASE_PATH + '物业后台账号-项目管理员拆分版.xlsx', {'company': 0, 'zone': 1, 'account': 2, 'pwd': 3})
        for row in xm:
            name = row['zone'] + '-管理员'
            print(Account._INSERT_USER_2222.format(account=row['account'], password=hashlib.md5(row['pwd'].encode('utf-8')).hexdigest(),
                                                   name=name, nickname=name, company_name=row['company'],
                                                   zone_name=row['zone']))
            print(Account._UPDATE_ZONE.format(account=row['account'], zone_name=row['zone']))
            print(Account._INSERT_R.format(account=row['account'], role_code='后台项目管理员'))
            print(Account._INSERT_CATEGORY.format(zone_name=row['zone']))
        print('COMMIT;')


if __name__ == '__main__':
    obj = Account()
    obj.handle()
