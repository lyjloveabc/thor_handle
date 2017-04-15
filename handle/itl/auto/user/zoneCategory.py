"""
修改category_id和category_name
"""


class ZoneCategory:
    __BASE_PATH = 'file/'

    def __init__(self):
        self.base_sql = 'update user set category_id = {category_id} where id = {id};'
        self.zone_category_group = dict()

        with open(ZoneCategory.__BASE_PATH + 'itl_zone_category.txt', 'r') as f:
            for line in f.readlines():
                line_split = line[:-1].split(',')
                zone_category = {
                    'id': line_split[0],
                    'zone_id': line_split[1],
                    'category_pool_id': line_split[2]
                }
                self.zone_category_group[zone_category['zone_id'] + ',' + zone_category['category_pool_id']] = zone_category['id']

    def handle(self):

        print('BEGIN;')
        with open(ZoneCategory.__BASE_PATH + 'user_simple.txt', 'r') as f:
            for line in f.readlines():
                line_split = line[:-1].split(',')
                user_simple = {
                    'id': line_split[0],
                    'category_id': line_split[1],
                    'zone_id': line_split[2]
                }
                print(self.base_sql.format(category_id=self.get_zone_category_id(user_simple), id=user_simple['id']))
        print('COMMIT;')

    def get_zone_category_id(self, user_simple):
        return self.zone_category_group[user_simple['zone_id'] + ',' + user_simple['category_id']]


if __name__ == '__main__':
    handle = ZoneCategory()
    handle.handle()

