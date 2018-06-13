"""
爱家端登录
select subscription_enter.id, house_info.house, house_info.building, house_info.door
from subscription_enter
left join house_info on house_info.id = subscription_enter.house_info_id
where period_id = 381;
"""
import datetime
import json

import requests

from utils.constant import constant
from utils.constant.constant import Constant
from utils.file.excel.readUtil import ReadUtil


class HandleWater:
    def __init__(self):
        self.today = datetime.datetime.now()
        self.today_int = int(self.today.strftime('%Y%m%d'))
        self.file_date_str = '_' + str(self.today_int)

        self.detail_json = '{"last_num":0.0,"lastdate":"","current_num":0.0,"currentdate":"","actualUse":0.0,"unitPrice":2.95}'
        self.sql = 'UPDATE subscription_enter SET status = \'ENTER\', detail = \'("last_num":{last},"lastdate":"{last_date}","current_num":{curr},"currentdate":"{curr_date}","actualUse":{actual},"unitPrice":2.95)\' WHERE id = {id};'

    def h(self):
        wm = dict()

        water = ReadUtil.read_file('南城景园住宅水费2018.2.1-2018.6.3（新）_data.xlsx', {'house': 0, 'base': 1, 'next': 2})
        for row in water:
            wm[row['house']] = row

        with open('南城5月份水费能耗数据.txt', 'r') as f:
            print(Constant.SQL_BEGIN)
            for row in f.readlines():
                row = row.replace('\n', '')
                array = row.split(',')
                key = str(int(array[1])) + '-' + str(int(array[2])) + '-' + str(int(array[3]))
                if key in wm:
                    # if float(wm[key]['next']) - float(wm[key]['base']) == 0:
                    #     print('房号:', key, '底数:', wm[key]['base'], '本期读数:', wm[key]['next'])
                    print(
                        self.sql.format(
                            last=float(wm[key]['base']), last_date='2018-04-30',
                            curr=float(wm[key]['next']), curr_date='2018-05-30',
                            actual=float(wm[key]['next']) - float(wm[key]['base']),
                            id=array[0]
                        ).replace('(', '{').replace(')', '}')
                    )
                else:
                    pass
            print(Constant.SQL_COMMIT)


if __name__ == '__main__':
    hw = HandleWater()
    hw.h()
