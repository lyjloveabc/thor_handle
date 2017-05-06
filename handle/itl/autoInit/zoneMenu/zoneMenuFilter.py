"""
select name, menu_ids from itl_menu_group;
"""
from utils.constant.constant import Constant


class ZoneMenuFilter:
    def __init__(self):
        pass

    @staticmethod
    def handle(zone_ids, data):
        if len(zone_ids) < 1:
            return

        sql = 'insert into itl_zone_menu_filter(gmt_create, gmt_modify, zone_id, menu_group_ids, menu_ids)' \
              'values (now(), now(), "{zone_id}", "{menu_group_ids}", "{menu_ids}");'

        menu_group_group = ZoneMenuFilter.get_menu_group(Constant.BASE_PATH + 'menuGroup_20170506.txt')

        print(Constant.SQL_BEGIN)
        for zone_id in zone_ids:
            menu_group_ids = ['3']
            menu_ids = list()

            if zone_id in data:
                menu_group_ids.extend(data[zone_id])
            for menu_group_id in menu_group_ids:
                menu_ids.extend(menu_group_group[menu_group_id])
            print(sql.format(zone_id=zone_id, menu_group_ids=','.join(menu_group_ids), menu_ids=','.join(menu_ids)))
        print(Constant.SQL_COMMIT)

    @staticmethod
    def get_menu_group(file):
        menu_group = dict()
        with open(file, 'r') as f:
            for line in f.readlines():
                line_split = line[:-1].split(';')
                menu_group[line_split[0]] = line_split[1].split(',')
        return menu_group


if __name__ == '__main__':
    zone_ids = ['1', '2', '5'] + [str(x) for x in range(9, 24)]

    data = dict()
    with open(Constant.BASE_PATH + 'arki整理的小区信息.txt', 'r') as f:
        for line in f.readlines():
            line_split = line[:-1].split(' ')
            data[line_split[0]] = line_split[1].split(',')

    menuGroup = ZoneMenuFilter()
    menuGroup.handle(zone_ids, data)
