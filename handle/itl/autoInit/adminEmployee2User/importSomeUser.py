"""
根据admin_employee数据，导入user数据
"""
import os


class ImportSomeUser:
    DAY = '_20170717'
    BASE_PATH = 'file/' + DAY + '/'

    def __init__(self):
        self.base_sql = 'insert into user' \
                        '(gmt_create, gmt_modify, account, password, name, identity_card, nickname,' \
                        'sex, mobile, avatar_url, address, email, emergency_contact,' \
                        'emergency_mobile, last_login_time, last_login_ip, category_id,' \
                        'category_name, company_id, zone_id, zone_ids, is_on_job, departure_time,' \
                        'job_title_id, job_title_name, old_user_id) ' \
                        'values ' \
                        '(now(), now(), "{account}", "{password}", "{name}", "{identity_card}", "{nickname}",' \
                        '"{sex}", "{mobile}", "{avatar_url}", "{address}", "{email}", "{emergency_contact}",' \
                        '"{emergency_mobile}", "{last_login_time}", "{last_login_ip}", "{category_id}",' \
                        '"{category_name}", "{company_id}", {zone_id}, "{zone_ids}", "{is_on_job}", "{departure_time}",' \
                        '"{job_title_id}", "{job_title_name}", "{old_user_id}");'

        if not os.path.exists(ImportSomeUser.BASE_PATH):
            os.mkdir(ImportSomeUser.BASE_PATH)

    def handle(self):
        mobile_group = set()
        admin_employee_group = ImportSomeUser.get_admin_employee_group()
        zone_category_group = ImportSomeUser.get_zone_category_group()

        with open(ImportSomeUser.BASE_PATH + 'ImportSomeUser_out' + ImportSomeUser.DAY + '.sql', 'w') as f:
            f.write('BEGIN;\n')

            admin_employee_group_keys = admin_employee_group.keys()
            for key in admin_employee_group_keys:
                if key in mobile_group:
                    continue
                admin_employee = admin_employee_group[key]

                admin_employee['type'] = 7 if admin_employee['type'] == '0' else admin_employee['type']
                admin_employee['name'] = str(admin_employee['name']).replace('"', '')
                admin_employee['Idcard'] = str(admin_employee['Idcard']).replace('"', '')
                sql = self.base_sql.format(account=key, password=admin_employee['password'], name=admin_employee['name'],
                                           identity_card=admin_employee['Idcard'], nickname=admin_employee['name'],
                                           sex='M' if admin_employee['sex'] == '1' else 'F', mobile=key,
                                           avatar_url=admin_employee['avtar'], address=admin_employee['address'],
                                           email='', emergency_contact=admin_employee['emergency_name'],
                                           emergency_mobile=admin_employee['emergency_mobile'],
                                           last_login_time='1970-01-01 00:00:01', last_login_ip='127.0.0.1',
                                           category_id=str(zone_category_group[admin_employee['zone_id'] + ',' + str(admin_employee['type'])]['id']),
                                           category_name=zone_category_group[admin_employee['zone_id'] + ',' + str(admin_employee['type'])]['name'],
                                           company_id=admin_employee['cid'],
                                           zone_id=admin_employee['zone_id'], zone_ids=admin_employee['zone_id'],
                                           is_on_job=0 if admin_employee['zone_id'] == '5' else 1,
                                           departure_time='1970-01-01 00:00:01',
                                           job_title_id='0', job_title_name=admin_employee['job_post_name'],
                                           old_user_id=admin_employee['id'])
                mobile_group.add(key)
                f.write(sql + '\n')

            f.write('COMMIT;\n')

    @staticmethod
    def get_admin_employee_group():
        old_user_group = dict()

        with open(ImportSomeUser.BASE_PATH + 'admin_employee_some' + ImportSomeUser.DAY + '.txt', 'r') as f:
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
                            'day_time2': temp[32],
                            'job_post_name': temp[33],
                            }
                if old_user['mobile'] == '':
                    print('没有mobile: ', old_user['id'])
                else:
                    old_user_group[old_user['mobile']] = old_user
        return old_user_group

    @staticmethod
    def get_zone_category_group():
        """
        sql: select id, zone_id, category_pool_id, category_pool_name from itl_zone_category;
        """
        zone_category_group = dict()

        with open(ImportSomeUser.BASE_PATH + 'itl_zone_category' + ImportSomeUser.DAY + '.txt', 'r') as f:
            for line in f.readlines():
                line_split = line[:-1].split(';')
                zone_category = {
                    'id': line_split[0],
                    'zone_id': line_split[1],
                    'category_pool_id': line_split[2],
                    'category_pool_name': line_split[3]
                }
                zone_category_group[zone_category['zone_id'] + ','
                                    + zone_category['category_pool_id']] \
                    = {'id': zone_category['id'], 'name': zone_category['category_pool_name']}
        return zone_category_group


if __name__ == '__main__':
    handle = ImportSomeUser()
    handle.handle()
