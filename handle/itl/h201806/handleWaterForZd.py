"""
爱家端登录
select subscription_enter.id, house_info.house, house_info.building, house_info.door
from subscription_enter
left join house_info on house_info.id = subscription_enter.house_info_id
where period_id = 423;
"""
import datetime
from utils.constant.constant import Constant
from utils.file.excel.readUtil import ReadUtil


class HandleWaterForZd:
    def __init__(self):
        self.today = datetime.datetime.now()
        self.today_int = int(self.today.strftime('%Y%m%d'))
        self.file_date_str = '_' + str(self.today_int)

        self.detail_json = '{"last_num":0.0,"lastdate":"","current_num":0.0,"currentdate":"","actualUse":0.0,"unitPrice":2.35}'
        self.sql = 'UPDATE subscription_enter SET status = \'NO_ENTER\', detail = \'("last_num":{last},"lastdate":"{last_date}","current_num":{curr},"currentdate":"{curr_date}","actualUse":{actual},"unitPrice":2.95)\' WHERE id = {id};'

    def h(self):
        wm = dict()

        water = ReadUtil.read_file('浙地水费底数（5月抄表）_data.xlsx', {'house': 0, 'base': 1})
        for row in water:
            wm[row['house']] = row

        with open('这地6月份水费能耗数据.txt.txt', 'r') as f:
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
                            last=float(wm[key]['base']), last_date='2018-05-06',
                            curr=0.00, curr_date='',
                            actual=0.00,
                            id=array[0]
                        ).replace('(', '{').replace(')', '}')
                    )
                else:
                    pass
            print(Constant.SQL_COMMIT)


if __name__ == '__main__':
    hw = HandleWaterForZd()
    hw.h()
