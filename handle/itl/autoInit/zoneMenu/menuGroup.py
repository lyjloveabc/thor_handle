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
    def get_menu(file):
        menu_group = dict()
        with open(file, 'r') as f:
            for line in f.readlines():
                line_split = line[:-1].split(';')
                menu_group[line_split[1]] = {'id': line_split[0], 'name': line_split[1]}
        return menu_group


if __name__ == '__main__':
    name = '111'
    data = ['报修派工', '出入管理']

    menuGroup = MenuGroup()
    menuGroup.handle(name, data)
