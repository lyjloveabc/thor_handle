# encoding=utf-8
"""
景江苑水费抄表初始化数据
"""
import re

from utils.ExcelReadUtil import ExcelReadUtil

__AUTHOR = 'thor'


class JjyWater_9_10(object):
    __BASE_PATH = 'file/'

    def __init__(self):
        self.field_index_dict = {
            'house_code': 0,
            'september_num': 1,
            'october_num': 2,
        }
        pass

    def handle(self):
        data = ExcelReadUtil.read_file(JjyWater_9_10.__BASE_PATH + '景江苑水费抄表初始化数据.xlsx', self.field_index_dict)

        house_info_group = dict()
        with open(JjyWater_9_10.__BASE_PATH + 'houseInfo20161123.txt', 'r') as f:
            for line in f.readlines():
                house_info_split = re.split(',', line[:-1])
                value = house_info_split[1] + house_info_split[2] + house_info_split[3]
                house_info_group[value] = house_info_split[0]

        pre_sql = "INSERT INTO subscription_enter(zone_id, sub_id, house_info_id, name, product_type_code, " \
                  "gmt_create, gmt_modify, detail, status, hasbill, period_id) VALUES "
        base_sql = '(2, 4, %d, "水费 2016年10月", "water", now(), now(), ' \
                   '\'{"last_num":%d,"lastdate":"2016-09-25","current_num":%d,"currentdate":"2016-10-25","actualUse":%d,"unitPrice":%.2f}\', ' \
                   '"ENTER", "NO_BILL", 4),'

        print(pre_sql)
        for item in data:
            house_code_split = re.split('-', item['house_code'])
            code = house_code_split[0] + house_code_split[1] + self.to4(house_code_split[2])

            if item['october_num'] == '未抄':
                unit_price = 0
                october_num = 0
            else:
                unit_price = float(item['october_num']) - float(item['september_num'])
                october_num = item['october_num']
            print(base_sql % (int(house_info_group[code]), item['september_num'], october_num, unit_price, 2.95))

    @staticmethod
    def to4(temp):
        if len(temp) == 3:
            temp = '0' + temp
        return temp


if __name__ == '__main__':
    handle = JjyWater_9_10()
    handle.handle()
