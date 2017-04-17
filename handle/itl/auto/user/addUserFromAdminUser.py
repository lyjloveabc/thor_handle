"""
从天眼账户添加用户
"""


class AddUserFromAdminUser(object):
    __BASE_PATH = 'file/'

    def __init__(self):
        self.base_sql = 'insert into user(gmt_create, gmt_modify, account, password, name, identity_card, nickname, sex, mobile, avatar_url, ' \
                        'address, email, emergency_contact, emergency_mobile, last_login_time, last_login_ip, category_name, ' \
                        'company_id, zone_id, zone_ids, is_on_job, departure_time, job_title_id, job_title_name) ' \
                        'values (now(), now(), "{account}", "{password}", "{name}", "{identity_card}", "{nickname}", "{sex}", "{mobile}", "{avatar_url}", ' \
                        '"{address}", "{email}", "{emergency_contact}", "{emergency_mobile}", "{last_login_time}", "{last_login_ip}",' \
                        '"{category_name}", -1,{zone_id}, "{zone_ids}", "{is_on_job}", "{departure_time}", "{job_title_id}", "{job_title_name}");'

    def handle(self):
        old_user_group = AddUserFromAdminUser.get_old_user_group()
        already_exist_mobile = AddUserFromAdminUser.get_already_exist_mobile()

        with open(AddUserFromAdminUser.__BASE_PATH + 'AddUserFromAdminUser_out.sql', 'w') as f:
            f.write('BEGIN;\n')
            keys = old_user_group.keys()
            for key in keys:
                if key not in already_exist_mobile:
                    old_user = old_user_group[key]
                    sql = self.base_sql.format(account=key, password=old_user['password'], name=old_user['nickname'],
                                               identity_card='', nickname=old_user['nickname'], sex='',
                                               mobile=key, avatar_url='', address='', email='', emergency_contact='', emergency_mobile='',
                                               last_login_time='1970-01-01 00:00:01', last_login_ip='',
                                               category_name='',
                                               zone_id=old_user['zone_id'], zone_ids=old_user['zone_id'], is_on_job='1', departure_time='1970-01-01 00:00:01',
                                               job_title_id='0',
                                               job_title_name='')
                    f.write(sql + '\n')
            f.write('COMMIT;\n')

    @staticmethod
    def get_old_user_group():
        old_user_group = dict()
        with open(AddUserFromAdminUser.__BASE_PATH + '天眼账户.txt', 'r') as f:
            for line in f.readlines():
                temp = line[:-1].split(';')
                old_user = {
                    'mobile': temp[0],
                    'nickname': temp[1],
                    'password': temp[2],
                    'zone_id': temp[3],
                    'zone_ids': temp[4]
                }
                old_user_group[old_user['mobile']] = old_user
        return old_user_group

    @staticmethod
    def get_already_exist_mobile():
        already_exist_mobile_group = set()
        with open(AddUserFromAdminUser.__BASE_PATH + 'user已经存在的mobile.txt', 'r') as f:
            for line in f.readlines():
                already_exist_mobile_group.add(line[:-1])
        return already_exist_mobile_group


if __name__ == '__main__':
    handle = AddUserFromAdminUser()
    handle.handle()


# select mobile, nickname, password, zone_id, zone_ids
# from admin_user
