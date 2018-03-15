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

        # 员工部门
        self.insert_user_cate = "INSERT INTO itl_user_category_relation(created_time, modified_time, user_id, zone_category_id, zone_category_name, zone_id) VALUES" \
                                " (now(), now(), {user_id}, {zone_category_id}, '{zone_category_name}', {zone_id});"

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
            {'id': 8, 'category': '总经办'},
        ]

    def h(self, file):
        zone_category_map = dict()

        # 公明物业的总部小区ID
        hq_zone_id = self.dao.get_one('SELECT hq_zone_id FROM itl_company WHERE id = 1;')['hq_zone_id']

        # 公明的总部小区所有的部门
        zone_category_list = self.dao.get_all('SELECT id, category_pool_name FROM itl_zone_category WHERE zone_id = "{zone_id}";'.format(zone_id=hq_zone_id))
        for row in zone_category_list:
            zone_category_map[row['category_pool_name']] = row['id']

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
