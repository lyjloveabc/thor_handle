"""
itl_company
zones
"""


class BatchCreateHqZone:
    def __init__(self, dao):
        self.dao = dao

        self.insert_sql = "INSERT INTO zones " \
                          "(id, name, description, buildtime, total_area, houses, address, service, helpme, " \
                          "seal_icon, funds, property_fee, cars_fee, energy, status, enter_time, off_time, cars_num, " \
                          "perm_house, rent_house, shop_house, leave_house, company_id, manager_id, shoufeiguize_content) " \
                          "VALUES ('{id}', '总部小区', '{description}', '2016-10-01', '0', 0, '', '', '', '', " \
                          "0.00, 0.00, 0.00, 0.00, 0, 1475251200, 1495555200, 0, 0, 0, 0, 0, '{company_id}', '{manager_id}', '');"

        self.insert_category_sql = """
                          INSERT INTO itl_zone_category (gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name, leader_user_ids) 
                          VALUES (now(), now(), '{zone_id}', '{category_pool_id}', '{category_pool_name}', NULL);
                          """

        self.update_sql = """
                          UPDATE itl_company SET hq_zone_id = '{hq_zone_id}' WHERE id = '{id}';
                          """

        self.category = dict()
        self.category[21] = '总经办'
        self.category[22] = '市场部'
        self.category[23] = '财务部'
        self.category[24] = '人事部'
        self.category[25] = '行政部'
        self.category[26] = '人力资源和行政部'
        self.category[27] = '项目管理部'
        self.category[28] = '项目运营部'
        self.category[29] = '项目品质部'
        self.category[30] = '研发部'
        self.category[31] = '产品运营部'

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
                f.write(self.insert_sql.format(id=zone_id, description=row['alias'], company_id=row['id'], manager_id=row['manager_id']))
                f.write('\n')

                # 更新公司的总部小区ID
                f.write(self.update_sql.format(id=row['id'], hq_zone_id=zone_id))
                f.write('\n')

                # 总部小区新增部门
                if row['id'] == 1:
                    for key, value in self.category.items():
                        f.write(self.insert_category_sql.format(zone_id=zone_id, category_pool_id=key, category_pool_name=value))
                        f.write('\n')
                else:
                    f.write(self.insert_category_sql.format(zone_id=zone_id, category_pool_id=27, category_pool_name=self.category[27]))
                    f.write('\n')
                zone_id += 1
            f.write('\n')

            # 总部人员迁移到这个小区
