"""
公明总部小区人员
"""


class HqUser:
    def __init__(self, dao):
        self.dao = dao

        # 删除该人的所有任务
        self.delete_task_sql = "DELETE FROM itl_user_task WHERE user_id = {user_id};"

        # 删除该人的当前所有小区
        self.delete_user_zone_sql = "DELETE FROM itl_user_zone_relation WHERE user_id = {user_id};"

        # 公明公司人员添加小区
        self.insert_user_zone = "INSERT INTO itl_user_zone_relation(created_time, modified_time, user_id, zone_id) VALUES (now(), now(), {user_id}, {zone_id});"

        # 更新用户信息
        self.update_user = "UPDATE user SET zone_id = {zone_id}, zone_ids = '{zone_ids}', category_id = {category_id}, category_name = '{category_name}' WHERE id = {id};"

        # 更新用户信息
        self.update_user_job_title = "UPDATE user SET job_title_id = 19, job_title_name = '总部领导' WHERE id = {id} AND job_title_id < 19;"

        # 员工部门
        self.insert_user_cate = "INSERT INTO itl_user_category_relation(created_time, modified_time, user_id, zone_category_id, zone_category_name, zone_id) VALUES" \
                                " (now(), now(), {user_id}, {zone_category_id}, '{zone_category_name}', {zone_id});"

        # 插入用户职能数据
        self.insert_role_sql = "INSERT INTO itl_user_role_relation(created_time, modified_time, user_id, role_code, zone_id) " \
                               "VALUES (now(), now(), '{user_id}', '{role_code}', '{zone_id}');"

        # 公明物业的总部人员
        self.hq_user_list = [
            {'id': '400', 'category': '研发部'},
            {'id': '454', 'category': '市场部'},
            {'id': '502', 'category': '项目品质部'},
            {'id': '618', 'category': '产品运营部'},
            {'id': '791', 'category': '产品运营部'},
            {'id': '1120', 'category': '产品运营部'},
            {'id': '1724', 'category': '产品运营部'},
            {'id': '1836', 'category': '财务部'},
            {'id': '1883', 'category': '项目品质部'},
            {'id': '1888', 'category': '产品运营部'},
            {'id': '1893', 'category': '项目管理部'},
            {'id': '1927', 'category': '项目品质部'},
            {'id': '1943', 'category': '项目品质部'},
            {'id': '1947', 'category': '项目管理部'},
            {'id': '1952', 'category': '研发部'},
            {'id': '1957', 'category': '项目管理部'},
            {'id': '2049', 'category': '项目品质部'},
            {'id': '2068', 'category': '项目管理部'},
            {'id': '2143', 'category': '项目品质部'},
            {'id': '2144', 'category': '项目品质部'},
            {'id': '2148', 'category': '人力资源和行政部'},
            {'id': '2149', 'category': '人力资源和行政部'},
            {'id': '2150', 'category': '人力资源和行政部'},
            {'id': '2151', 'category': '人力资源和行政部'},
            {'id': '2202', 'category': '项目品质部'},
            {'id': '2254', 'category': '总经办'},
            {'id': '8', 'category': '总经办'}
        ]

        # 公明物业的需要所有小区的人员
        self.all_zone_list = [
            {'id': 2202, 'category': ['工程维修', '工程部'], 'role': '工程'},
            {'id': 1883, 'category': ['工程维修', '工程部'], 'role': '工程负责人'},
            {'id': 1927, 'category': ['保安部'], 'role': '保安负责人'},
            {'id': 1943, 'category': ['环境部', '绿化'], 'role': '绿化负责人'},
            {'id': 2143, 'category': ['工程维修', '工程部'], 'role': '工程'},
            {'id': 2144, 'category': ['工程维修', '工程部'], 'role': '工程'},
            {'id': 2049, 'category': ['保安部'], 'role': '保安负责人'},
            {'id': 502, 'category': ['服务中心'], 'role': '项目负责人'},
        ]

    def h(self, file):
        # 公明物业的总部小区ID
        hq_zone_id = self.dao.get_one('SELECT hq_zone_id FROM itl_company WHERE id = 1;')['hq_zone_id']

        zone_list = self.dao.get_all('SELECT id FROM zones WHERE company_id = 1 AND id != (SELECT hq_zone_id FROM itl_company WHERE id =1);')

        # 公明的总部小区所有的部门
        zone_category_map = dict()
        zone_category_list = self.dao.get_all('SELECT id, category_pool_name FROM itl_zone_category WHERE zone_id = "{zone_id}";'.format(zone_id=hq_zone_id))
        for row in zone_category_list:
            zone_category_map[row['category_pool_name']] = row['id']

        # 非-公明的总部小区所有的部门
        zc_map = dict()
        zc_list = self.dao.get_all(
            'SELECT id, category_pool_name, zone_id FROM itl_zone_category WHERE zone_id IN ( SELECT id FROM zones WHERE company_id = 1 AND id != (SELECT hq_zone_id FROM itl_company WHERE id =1));'
        )
        for row in zc_list:
            key = str(row['zone_id']) + '-' + row['category_pool_name']
            zc_map[key] = row['id']

        with open(file, 'a') as f:
            f.write('\n')
            f.write('# 处理公明物业的所有总部人员')
            f.write('\n')

            for row in self.hq_user_list:
                # 删除他的任务
                f.write(self.delete_task_sql.format(user_id=row['id']))
                f.write('\n')

                # 删除他的小区
                f.write(self.delete_user_zone_sql.format(user_id=row['id']))
                f.write('\n')

                # 添加user_zone记录
                f.write(self.insert_user_zone.format(user_id=row['id'], zone_id=hq_zone_id))
                f.write('\n')

                # 更新用户信息
                f.write(
                    self.update_user.format(zone_id=hq_zone_id, zone_ids=hq_zone_id, category_id=zone_category_map[row['category']], category_name=row['category'], id=row['id'])
                )
                f.write('\n')

                # 添加user_zone记录
                f.write(
                    self.insert_user_cate.format(user_id=row['id'], zone_category_id=zone_category_map[row['category']], zone_category_name=row['category'], zone_id=hq_zone_id)
                )
                f.write('\n')

                # 更新用户头衔
                f.write(
                    self.update_user_job_title.format(id=row['id'])
                )
                f.write('\n')

                # 总部小区的人员处理
                user_role_list = self.dao.get_all('SELECT id, role_code FROM user_role_relation WHERE user_id = ' + str(row['id']) + ';')
                for user_role in user_role_list:
                    f.write(self.insert_role_sql.format(user_id=row['id'], role_code=user_role['role_code'], zone_id=hq_zone_id))
                    f.write('\n')

            for x in self.all_zone_list:
                for zone in zone_list:
                    f.write(self.insert_user_zone.format(user_id=x['id'], zone_id=zone['id']))
                    f.write('\n')

                    f.write(self.insert_role_sql.format(user_id=x['id'], role_code=x['role'], zone_id=zone['id']))
                    f.write('\n')

                    for cate in list(x['category']):
                        print(cate)
                        key = str(zone['id']) + '-' + cate
                        if key in zc_map.keys():
                            f.write(
                                self.insert_user_cate.format(user_id=x['id'], zone_category_id=zc_map[key], zone_category_name=cate,
                                                             zone_id=zone['id'])
                            )
                            f.write('\n')
