"""
公明总部小区人员
"""


class HqUser:
    def __init__(self, dao):
        self.dao = dao

        self.hq_user = [
            {'id': 8, 'category': '总经办'},
        ]

        self.delete_task_sql = "DELETE FROM itl_user_task WHERE user_id = '{user_id}';"
        self.delete_user_zone_sql = "DELETE FROM itl_user_zone_relation WHERE user_id = '{user_id}';"

    def h(self, file):
        with open(file, 'a') as f:
            f.write('\n')
            f.write('# 处理公明物业的所有总部人员')
            f.write('\n')

            for row in self.hq_user:
                # 删除他的任务
                f.write(self.delete_task_sql.format(user_id=row['id']))
                f.write('\n')

                # 删除他的小区
                f.write(self.delete_user_zone_sql.format(user_id=row['id']))
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
