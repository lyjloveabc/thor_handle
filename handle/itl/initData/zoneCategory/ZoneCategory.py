"""
第一次权限模块（外加新管家首页、工具，加分扣分）初始化小区分类数据
"""


class ZoneCategory(object):
    __BASE_PATH = 'file/'

    def __init__(self):
        pass

    @staticmethod
    def handle():
        zone_ids = ["1", "2", "5", "9", "10", "11", "12"]
        for zId in zone_ids:
            sql = "insert into zone_category(zone_id, category_id, category_name) values(" + zId + ", 1, '绿化');"
            print(sql)
            sql = "insert into zone_category(zone_id, category_id, category_name) values(" + zId + ", 2, '清洁');"
            print(sql)
            sql = "insert into zone_category(zone_id, category_id, category_name) values(" + zId + ", 3, '工程维修');"
            print(sql)
            sql = "insert into zone_category(zone_id, category_id, category_name) values(" + zId + ", 4, '安保');"
            print(sql)
            sql = "insert into zone_category(zone_id, category_id, category_name) values(" + zId + ", 5, '电梯');"
            print(sql)
            sql = "insert into zone_category(zone_id, category_id, category_name) values(" + zId + ", 6, '服务中心');"
            print(sql)
            sql = "insert into zone_category(zone_id, category_id, category_name) values(" + zId + ", 7, '其他');"
            print(sql)
            sql = "insert into zone_category(zone_id, category_id, category_name) values(" + zId + ", 8, '邻里');"
            print(sql)
            sql = "insert into zone_category(zone_id, category_id, category_name) values(" + zId + ", 9, '室内维修');"
            print(sql)


if __name__ == '__main__':
    handle = ZoneCategory()
    handle.handle()