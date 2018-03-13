"""
公明总部小区人员
"""


class HqUser:
    def __init__(self, dao):
        self.dao = dao

        # 删除该人的所有任务
        self.delete_task_sql = "DELETE FROM itl_user_task WHERE user_id = '{user_id}';"

        # 删除该人的当前所有小区
        self.delete_user_zone_sql = "DELETE FROM itl_user_zone_relation WHERE user_id = '{user_id}';"

        # 公明公司人员添加小区
        self.insert_user_zone = "INSERT INTO itl_user_zone_relation(created_time, modified_time, user_id, zone_id) VALUES (now(), now(), '{user_id}', '{zone_id}');"

        # 员工部门
        self.insert_user_cate = "INSERT INTO itl_user_category_relation(created_time, modified_time, user_id, zone_category_id, zone_category_name, zone_id) VALUES" \
                                " (now(), now(), '{user_id}', '{zone_category_id}', '{zone_category_name}', '{zone_id}');"

        # 公明物业的总部人员
        self.hq_user_list = [
            {'id': 8, 'category': '总经办'},
        ]

        # 公明物业的需要所有小区的人员
        self.hq_user_list = [
            {'id': 8, 'category': '总经办'},
        ]

    def h(self, file):
        company = self.dao.get_all('SELECT id, alias, manager_id FROM itl_company ORDER BY id;')  # 获取所有的公司
        start_id = int(self.dao.get_one('SELECT max(id) AS max_id FROM zones;')['max_id'])  # 获取当前小区ID的最大值
        zone_id = start_id + 1

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
                f.write(self.insert_user_zone.format(user_id=row['id'], zone_id=2222222222))
                f.write('\n')

                # 添加user_zone记录
                f.write(self.insert_user_cate.format(user_id=row['id'], zone_id=2222222222))
                f.write('\n')

            company = self.dao.get_all('SELECT id, alias, manager_id FROM itl_company ORDER BY id;')  # 获取所有的公司
        start_id = int(self.dao.get_one('SELECT max(id) AS max_id FROM zones;')['max_id'])  # 获取当前小区ID的最大值

        # 根据所有公司创建总部小区
        with open(file, 'a') as f:
            f.write('\n')
            f.write('# 根据所有公司创建总部小区')
            f.write('\n')
            for row in company:
                f.write(self.insert_sql.format(id=start_id, description=row['alias'], company_id=row['id'], manager_id=row['manager_id']))
                f.write('\n')
                start_id += 1
            f.write('\n')

            # 总部人员迁移到这个小区
