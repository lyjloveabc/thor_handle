# encoding=utf-8
"""
需要处理的房号ID
"""
import re

__AUTHOR = 'thor'


class HouseId(object):
    __BASE_PATH = 'file/'

    def __init__(self):
        self.field_index_dict = {
            'house_code': 0,
            'september_num': 1,
            'october_num': 2,
        }

    def handle(self):
        per_sql = 'select id from house_info where zone_id = 2 and ( '
        print(per_sql)

        with open(HouseId.__BASE_PATH + 'houseInfo.txt', 'r') as f:
            for line in f.readlines():
                original_split = re.split(',', line[:-1])
                house_info_split = re.split('-', original_split[0])
                print(' (house = {house} and building = {building} and door = {door}) or'
                      .format(house=house_info_split[0], building=house_info_split[1], door=house_info_split[2]))
        print(');')

    @staticmethod
    def to4(temp):
        if len(temp) == 3:
            temp = '0' + temp
        return temp


if __name__ == '__main__':
    handle = HouseId()
    handle.handle()

# select id from house_info where zone_id = 2 and (
#  (house = 1 and building = 1 and door = 1701) or
#  (house = 4 and building = 1 and door = 1002) or
#  (house = 5 and building = 1 and door = 902) or
#  (house = 8 and building = 2 and door = 501) or
#  (house = 8 and building = 2 and door = 601) or
#  (house = 8 and building = 2 and door = 602) or
#  (house = 9 and building = 2 and door = 301) or
#  (house = 6 and building = 1 and door = 101) or
#  (house = 6 and building = 1 and door = 102) or
#  (house = 6 and building = 2 and door = 101) or
#  (house = 6 and building = 2 and door = 102) or
#  (house = 7 and building = 1 and door = 101) or
#  (house = 7 and building = 1 and door = 102) or
#  (house = 7 and building = 2 and door = 101) or
#  (house = 7 and building = 2 and door = 102) or
#  (house = 8 and building = 1 and door = 101) or
#  (house = 8 and building = 1 and door = 102) or
#  (house = 8 and building = 2 and door = 101) or
#  (house = 8 and building = 2 and door = 102) or
#  (house = 9 and building = 1 and door = 101) or
#  (house = 9 and building = 1 and door = 102) or
#  (house = 9 and building = 1 and door = 1801) or
#  (house = 9 and building = 1 and door = 1802) or
#  (house = 9 and building = 2 and door = 101) or
#  (house = 9 and building = 2 and door = 102)
# );