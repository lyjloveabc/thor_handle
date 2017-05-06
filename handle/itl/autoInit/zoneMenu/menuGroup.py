"""
select id, name from permission where type = 'MENU';
"""
from utils.constant.constant import Constant


class MenuGroup:
    def __init__(self):
        pass

    @staticmethod
    def handle(menu_group_name, menu_names):
        if menu_group_name is None or menu_group_name == '' or len(menu_names) < 1:
            return

        sql = 'insert into itl_menu_group(gmt_create, gmt_modify, name, menu_ids)' \
              'values (now(), now(), "{name}", "{menu_ids}");'
        menu_ids = list()
        menu_group = MenuGroup.get_menu(Constant.BASE_PATH + 'menu_20170506.txt')

        for menu_name in menu_names:
            menu_ids.append(menu_group[menu_name]['id'])

        print(sql.format(name=menu_group_name, menu_ids=','.join(menu_ids)))

    @staticmethod
    def handle_with_file(data):
        if data is None or len(data) < 1:
            return

        sql = 'insert into itl_menu_group(gmt_create, gmt_modify, name, menu_ids)' \
              'values (now(), now(), "{name}", "{menu_ids}");'
        menu_group = MenuGroup.get_menu(Constant.BASE_PATH + 'menu_20170506.txt')

        print(Constant.SQL_BEGIN)
        keys = data.keys()
        for key in keys:
            menu_ids = list()
            for menu_name in data[key]:
                menu_ids.append(menu_group[menu_name]['id'])
            print(sql.format(name=key, menu_ids=','.join(menu_ids)))
        print(Constant.SQL_COMMIT)

    @staticmethod
    def get_menu(file):
        menu_group = dict()
        with open(file, 'r') as f:
            for line in f.readlines():
                line_split = line[:-1].split(';')
                menu_group[line_split[1]] = {'id': line_split[0], 'name': line_split[1]}
        return menu_group


if __name__ == '__main__':
    # name = '111'
    # data = ['报修派工', '出入管理']

    data = dict()
    with open(Constant.BASE_PATH + 'arki整理-20170506.txt', 'r') as f:
        for line in f.readlines():
            line_split = line[:-1].split(' ')
            data[line_split[0]] = line_split[1].split(',')

    menuGroup = MenuGroup()
    menuGroup.handle_with_file(data)
