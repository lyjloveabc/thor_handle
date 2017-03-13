"""
景江苑水费抄表（
"""
import re
import xml.dom.minidom

__AUTHOR = 'thor'


class JjyWater_1701(object):
    __BASE_PATH = 'file/'

    def __init__(self):
        pass

    def handle(self):
        dom_tree = xml.dom.minidom.parse(JjyWater_1701.__BASE_PATH + "jjy1701.xml")
        collection = dom_tree.documentElement
        records = collection.getElementsByTagName("RECORD")

        for record in records:
            record_id = record.getElementsByTagName('id')[0].childNodes[0].data
            house_info_id = record.getElementsByTagName('house_info_id')[0].childNodes[0].data
            detail = record.getElementsByTagName('detail')[0].childNodes[0].data

            last_num = float(re.search(r'"last_num":(.+),"lastdate"', detail).group(1))
            new_detail = re.sub(r'"current_num":0.0', '"current_num":' + str(last_num), detail)
            new_detail = re.sub(r'"currentdate":""', '"currentdate":"2016-01-25"', new_detail)

            sql = 'update subscription_enter set detail = \'{new_detail}\', status = \'ENTER\' where id = {sub_enter_id};'.format(new_detail=new_detail,
                                                                                                                                  sub_enter_id=record_id)
            print(sql)

    @staticmethod
    def remove_pre_zero(param):
        return str(int(param))

    def get_enter_num(self, param):
        for sub_enter in self.source_sub_enter:
            if sub_enter['house_code'] == param:
                return sub_enter
        return None


if __name__ == '__main__':
    handle = JjyWater_1701()
    handle.handle()
