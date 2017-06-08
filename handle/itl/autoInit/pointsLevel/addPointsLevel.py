"""
小区加分等级
"""


class AddPointsLevel(object):
    __BASE_PATH = 'file/'

    def __init__(self):
        pass

    @staticmethod
    def handle(zone_ids):
        print('BEGIN;')
        for zId in zone_ids:
            sql = 'insert into bonus_points_level(gmt_create, gmt_modify, zone_id, min_add, max_add, min_cut, max_cut) ' \
                  'values(now(), now(), ' + zId + ', 0, 2, 2, 3);'
            print(sql)
        print('COMMIT;')


if __name__ == '__main__':
    # data = ['24', '25', '26', '27']
    data = ['1', '2', '5'] + [str(x) for x in range(9, 29)]

    handle = AddPointsLevel()
    handle.handle(data)
