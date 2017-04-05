"""
用户迁移（纯自动迁移）
"""


class OldUserToNewUser(object):
    __BASE_PATH = 'file/'

    def __init__(self):
        self.base_sql = 'insert into user(gmt_create, gmt_modify, account, password, name, identity_card, nickname, sex, mobile, avatar_url, ' \
                        'address, email, emergency_contact, emergency_mobile, last_login_time, last_login_ip, category_id, category_name, ' \
                        'company_id, zone_id, zone_ids, is_on_job, departure_time, job_title_id, job_title_name) ' \
                        'values (now(), now(), "{account}", "{password}", "{name}", "{identity_card}", "{nickname}", "{sex}", "{mobile}", "{avatar_url}", ' \
                        '"{address}", "{email}", "{emergency_contact}", "{emergency_mobile}", "{last_login_time}", "{last_login_ip}", "{category_id}", ' \
                        '"{category_name}", "{company_id}", {zone_id}, "{zone_ids}", "{is_on_job}", "{departure_time}", "{job_title_id}", "{job_title_name}");'

    def handle(self):
        old_user_group = OldUserToNewUser.get_old_user_group()
        category_group = OldUserToNewUser.get_category_group()

        with open(OldUserToNewUser.__BASE_PATH + 'out.sql', 'w') as f:
            f.write('BEGIN;\n')
            keys = old_user_group.keys()
            for key in keys:
                old_user = old_user_group[key]
                sex = 'M' if old_user['sex'] == '1' else 'F'
                category_name = '未知' if old_user['type'] == '0' else category_group[old_user['type']]
                sql = self.base_sql.format(account=key, password=old_user['password'], name=str(old_user['name']).replace('"', ''),
                                           identity_card=str(old_user['Idcard']).replace('"', ''), nickname=str(old_user['name']).replace('"', ''), sex=sex, mobile=key,
                                           avatar_url=old_user['avtar'], address=old_user['address'], email='',
                                           emergency_contact=old_user['emergency_name'], emergency_mobile=old_user['emergency_mobile'],
                                           last_login_time='1970-01-01 00:00:01', last_login_ip='', category_id=old_user['type'], category_name=category_name,
                                           company_id=old_user['cid'],
                                           zone_id=old_user['zone_id'], zone_ids=old_user['zone_id'], is_on_job='1', departure_time='1970-01-01 00:00:01',
                                           job_title_id='0',
                                           job_title_name='')
                f.write(sql + '\n')
            f.write('COMMIT;\n')

    @staticmethod
    def get_old_user_group():
        old_user_group = dict()
        with open(OldUserToNewUser.__BASE_PATH + 'oldUser.txt', 'r') as f:
            for line in f.readlines():
                temp = line[:-1].split(';')
                old_user = {'id': temp[0],
                            'cid': temp[1],
                            'type': temp[2],
                            'manager': temp[3],
                            'zone_id': temp[4],
                            'name': temp[5],
                            'job': temp[6],
                            'sex': temp[7],
                            'mobile': temp[8],
                            'emergency_mobile': temp[9],
                            'emergency_name': temp[10],
                            'password': temp[11],
                            'avtar': temp[12],
                            'address': temp[13],
                            'Idcard': temp[14],
                            'status': temp[15],
                            'is_employ': temp[16],
                            'work_status': temp[17],
                            'sort_num': temp[18],
                            'app_version': temp[19],
                            'device_type': temp[20],
                            'score': temp[21],
                            'level': temp[22],
                            'on_job': temp[23],
                            'in_list': temp[24],
                            'job_post_id': temp[25],
                            'jpid': temp[26],
                            'has_kpi': temp[27],
                            'switch': temp[28],
                            'role': temp[29],
                            'baas': temp[30],
                            'day_time': temp[31],
                            'day_time2': temp[32]
                            }
                if old_user['mobile'] == '':
                    print('没有mobile: ', old_user['id'])
                else:
                    old_user_group[old_user['mobile']] = old_user
        return old_user_group

    @staticmethod
    def get_company_group():
        company_group = dict()
        with open(OldUserToNewUser.__BASE_PATH + 'company.txt', 'r') as f:
            for line in f.readlines():
                temp = line[:-1].split(';')
                company = {
                    'id': temp[0],
                    'tid': temp[1],
                    'name': temp[2],
                    'description': temp[3],
                    'status': temp[4],
                }
                company_group[company['id']] = company
        return company_group

    @staticmethod
    def get_category_group():
        category_group = dict()
        with open(OldUserToNewUser.__BASE_PATH + 'admin_services_type.txt', 'r') as f:
            for line in f.readlines():
                temp = line[:-1].split(';')
                category = {
                    'id': temp[0],
                    'title': temp[1]
                }
                category_group[category['id']] = category['title']
        return category_group


if __name__ == '__main__':
    handle = OldUserToNewUser()
    handle.handle()
