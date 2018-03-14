"""
用户职能、部门统一处理
心累
"""


class RoleData:
    def __init__(self, dao):
        self.dao = dao

        # 插入用户职能数据
        self.insert_sql = "INSERT INTO itl_user_role_relation(created_time, modified_time, user_id, role_code, zone_id) " \
                          "VALUES (now(), now(), '{user_id}', '{role_code}', '{zone_id}');"

        # 插入用户部门数据
        self.insert_category_sql = "INSERT INTO itl_user_category_relation (gmt_create, gmt_modify, user_id, zone_category_id, zone_category_name, zone_id) " \
                                   "VALUES (now(), now(), '{user_id}', '{zone_category_id}', '{zone_category_name}', '{zone_id}');"

    def h(self, file):
        user_list = self.dao.get_all('SELECT id, category_id, category_name, zone_id FROM user;')
        uz_list = self.dao.get_all('SELECT user_id, zone_id FROM itl_user_zone_relation;')
        zc_list = self.dao.get_all('SELECT id, zone_id, category_pool_id, category_pool_name FROM itl_zone_category;')
        role_list = self.dao.get_all('SELECT user_id, role_code FROM user_role_relation;')

        uz_map = dict()
        for uz in uz_list:
            if uz['user_id'] not in uz_map.keys():
                uz_map[uz['user_id']] = list()
            uz_map[uz['user_id']].append(uz['zone_id'])

        zc_map = dict()
        for zc in zc_list:
            key = str(zc['category_pool_name']) + '-' + str(zc['zone_id'])
            zc_map[key] = zc['id']

        role_map = dict()
        for role in role_list:
            if role['user_id'] not in role_map.keys():
                role_map[role['user_id']] = list()
            role_map[role['user_id']].append(role['role_code'])

        # 根据所有公司创建总部小区
        with open(file, 'a') as f:
            f.write('\n')
            f.write('# 用户职能、部门统一处理')
            f.write('\n')
            for user in user_list:
                if user['id'] in uz_map.keys():
                    for user_zone in uz_map[user['id']]:
                        if user['id'] in role_map.keys():
                            for user_role in role_map[user['id']]:
                                f.write(self.insert_sql.format(user_id=user['id'], role_code=user_role, zone_id=user_zone))
                                f.write('\n')

                        if user['category_name'] != '' and user['category_name'] is not None:
                            zc_key = user['category_name'] + '-' + str(user_zone)

                            if zc_key in zc_map.keys():
                                f.write(
                                    self.insert_category_sql.format(user_id=user['id'], zone_category_id=zc_map[zc_key], zone_category_name=user['category_name'],
                                                                    zone_id=user_zone))
                                f.write('\n')
            f.write('\n')
