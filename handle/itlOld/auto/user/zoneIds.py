"""
用户迁移（纯自动迁移）
"""


class ZoneIds(object):
    __BASE_PATH = 'file/'

    def __init__(self):
        self.base_sql = 'update user set zone_ids = "{zone_ids}" where mobile = {mobile};'

    def handle(self):
        mobile_zone_ids = list()
        with open(ZoneIds.__BASE_PATH + 'admin_user_zone_ids.txt', 'r') as f:
            for line in f.readlines():
                line_split = line[:-1].split(';')
                item = {
                    'mobile': line_split[0],
                    'zone_ids': line_split[1]
                }
                mobile_zone_ids.append(item)

        with open(ZoneIds.__BASE_PATH + 'ZoneIds_out222.sql', 'w') as f:
            f.write('BEGIN;\n')
            size = len(mobile_zone_ids)
            for index in range(size):
                print(index)
                sql = self.base_sql.format(zone_ids=mobile_zone_ids[index]['zone_ids'], mobile=mobile_zone_ids[index]['mobile'])
                f.write(sql + '\n')
            f.write('COMMIT;\n')


if __name__ == '__main__':
    handle = ZoneIds()
    handle.handle()
