"""
添加属性
"""

__AUTHOR = 'thor'


class AddBonusPointsLevel:
    __BASE_PATH = 'file/'

    def __init__(self):
        self.base_sql = "INSERT INTO `bonus_points_level` VALUES " \
                        "('{id}', now(), now(), '{zone_id}', '{min_add}', '{max_add}', '{min_cut}', '{max_cut}');"

    def handle(self):
        print('BEGIN;')

        with open(AddBonusPointsLevel.__BASE_PATH + 'zones.txt') as f:
            index = 3
            for line in f.readlines():
                print(self.base_sql.format(id=index, zone_id=line[:-1], min_add=0, max_add=2, min_cut=2, max_cut=3))
                index += 1
        print('COMMIT;')


if __name__ == '__main__':
    handle = AddBonusPointsLevel()
    handle.handle()

# 扣分：-2，-3
# 加分：+2
