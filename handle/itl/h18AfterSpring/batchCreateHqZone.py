"""
select id, alias, manager_id from itl_company order by id;


"""


class BatchCreateHqZone:
    def __init__(self, dao):
        self.insert_sql = "INSERT INTO zones " \
                          "(id, name, description, buildtime, total_area, houses, address, service, helpme, " \
                          "seal_icon, funds, property_fee, cars_fee, energy, status, enter_time, off_time, cars_num, " \
                          "perm_house, rent_house, shop_house, leave_house, company_id, manager_id, shoufeiguize_content) " \
                          "VALUES ('{id}', '总部小区', '{description}', '2016-10-01', '0', 0, '', '', '', '', " \
                          "0.00, 0.00, 0.00, 0.00, 0, 1475251200, 1495555200, 0, 0, 0, 0, 0, '{company_id}', '{manager_id}', '');"
        self.dao = dao

    def h(self, file):
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
