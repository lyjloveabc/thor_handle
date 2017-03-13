"""
景江苑水费抄表（12-29景江苑抄表数据.xls）数据导入
"""
import re
import xml.dom.minidom

from utils.ExcelReadUtil import ExcelReadUtil

__AUTHOR = 'thor'


class JjyWater_12(object):
    __BASE_PATH = 'file/'

    def __init__(self):
        self.field_index_dict = {
            'house_code': 0,
            'november_num': 1,
            'december_num': 2,
        }
        self.source_sub_enter = ExcelReadUtil.read_file(JjyWater_12.__BASE_PATH + '12-29景江苑抄表数据.xls', self.field_index_dict)

    def handle(self):
        # 数据库中house_info数据
        house_info_group = dict()
        with open(JjyWater_12.__BASE_PATH + 'house_id_code_20161229.txt', 'r') as f:
            for line in f.readlines():
                house_info_split = re.split(',', line[:-1])
                key = house_info_split[0]
                value = house_info_split[1] + '-' + house_info_split[2] + '-' + self.remove_pre_zero(house_info_split[3])
                house_info_group[key] = value

        dom_tree = xml.dom.minidom.parse(JjyWater_12.__BASE_PATH + "sub_enter_12_20161229.xml")
        collection = dom_tree.documentElement
        records = collection.getElementsByTagName("RECORD")

        # 数据库中sub_enter_20161229数据:
        for record in records:
            record_id = record.getElementsByTagName('id')[0].childNodes[0].data
            house_info_id = record.getElementsByTagName('house_info_id')[0].childNodes[0].data
            detail = record.getElementsByTagName('detail')[0].childNodes[0].data

            enter_num = self.get_enter_num(house_info_group[house_info_id])
            if enter_num is None:
                print('delete from subscription_enter where id = ' + record_id + ';')
            else:
                actual_use = enter_num['december_num'] - float(re.search(r'"last_num":(.+),"lastdate"', detail).group(1))
                new_detail = re.sub(r'"current_num":0.0', '"current_num":' + str(enter_num['december_num']), detail)
                new_detail = re.sub(r'"currentdate":""', '"currentdate":"2016-12-25"', new_detail)
                new_detail = re.sub(r'"actualUse":0.0', '"actualUse":' + str(actual_use), new_detail)

                sql = 'update subscription_enter set detail = \'{new_detail}\', status = \'ENTER\' where id = {sub_enter_id};'.format(new_detail=new_detail, sub_enter_id=record_id)
                # print(sql)

    @staticmethod
    def remove_pre_zero(param):
        return str(int(param))

    def get_enter_num(self, param):
        for sub_enter in self.source_sub_enter:
            if sub_enter['house_code'] == param:
                return sub_enter
        return None


if __name__ == '__main__':
    handle = JjyWater_12()
    handle.handle()
