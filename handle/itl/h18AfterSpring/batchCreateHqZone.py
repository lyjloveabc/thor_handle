"""
itl_company
zones
"""


class BatchCreateHqZone:
    def __init__(self, dao):
        self.dao = dao

        # 插入总部小区
        self.insert_sql = "INSERT INTO zones " \
                          "(id, name, description, buildtime, total_area, houses, address, service, helpme, " \
                          "seal_icon, funds, property_fee, cars_fee, energy, status, enter_time, off_time, cars_num, " \
                          "perm_house, rent_house, shop_house, leave_house, company_id, manager_id, shoufeiguize_content) " \
                          "VALUES ('{id}', '{name}', '{description}', '2016-10-01', '0', 0, '', '', '', '', " \
                          "0.00, 0.00, 0.00, 0.00, 0, 1475251200, 1495555200, 0, 0, 0, 0, 0, '{company_id}', '{manager_id}', '');"

        # 插入总部小区的相关部门
        self.insert_category_sql = "INSERT INTO itl_zone_category (gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name, leader_user_ids) " \
                                   "VALUES (now(), now(), '{zone_id}', '{category_pool_id}', '{category_pool_name}', NULL);"

        # 更新公司的总部小区ID字段
        self.update_sql = "UPDATE itl_company SET hq_zone_id = '{hq_zone_id}' WHERE id = '{id}';"

        # 总部部门
        self.category_list = [
            {'id': 21, 'category': '总经办'},
            {'id': 22, 'category': '市场部'},
            {'id': 23, 'category': '财务部'},
            {'id': 26, 'category': '人力资源和行政部'},
            {'id': 27, 'category': '项目管理部'},
            {'id': 30, 'category': '研发部'},
            {'id': 31, 'category': '产品运营部'},
        ]

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

        # 根据所有公司创建总部小区
        with open(file, 'a') as f:
            f.write('\n')
            f.write('# 根据所有公司创建总部小区、更新公司的总部小区ID、总部小区新增部门')
            f.write('\n')

            for row in company:
                # 添加总部小区
                f.write(self.insert_sql.format(id=zone_id, name=row['alias'] + '-总部小区', description=row['alias'], company_id=row['id'], manager_id=row['manager_id']))
                f.write('\n')

                # 更新公司的总部小区ID
                f.write(self.update_sql.format(id=row['id'], hq_zone_id=zone_id))
                f.write('\n')

                # 总部小区新增部门
                if row['id'] == 1:  # 公明物业
                    for category in self.category_list:
                        f.write(self.insert_category_sql.format(zone_id=zone_id, category_pool_id=category['id'], category_pool_name=category['category']))
                        f.write('\n')
                else:
                    f.write(self.insert_category_sql.format(zone_id=zone_id, category_pool_id=27, category_pool_name='项目管理部'))
                    f.write('\n')
                zone_id += 1
            f.write('\n')
