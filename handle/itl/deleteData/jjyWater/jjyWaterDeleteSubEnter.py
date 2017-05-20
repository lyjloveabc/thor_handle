"""
删除景江苑多余的、无效的水费抄录记录

获取景江苑房屋信息：select id, house, building, door from house_info where zone_id = 2;

获取景江苑某一批次的sub_enter数据：
select id, house_info_id from subscription_enter
where subscription_enter.period_id = 69 and zone_id = 2
order by house_info_id;

"""
import re

from utils.constant.constant import Constant
from utils.system.systemUtil import SystemUtil


class JjyWaterDeleteSubEnter:
    def __init__(self):
        self.valid_house_info_group = set()  # 景江苑有效房户
        with open(Constant.BASE_PATH + 'valid_house_info.txt', 'r') as f:
            for line in f.readlines():
                self.valid_house_info_group.add(line[:-1])

        self.house_info_group = dict()  # 景江苑所有房户
        with open(Constant.BASE_PATH + 'jjyHouseInfo_20170520.txt', 'r') as f:
            for line in f.readlines():
                house_info_split = re.split(Constant.DEFAULT_SEP, line[:-1])
                key = house_info_split[0]
                value = house_info_split[1] + '-' + house_info_split[2] + '-' + SystemUtil.remove_pre_zero(house_info_split[3])
                self.house_info_group[key] = value

    def handle(self, period):
        sub_enter_group = list()  # 抄表数据
        with open(Constant.BASE_PATH + 'jjyWater-' + period + '.txt', 'r') as f:
            for line in f.readlines():
                line_split = line[:-1].split(Constant.DEFAULT_SEP)
                sub_enter_group.append({'id': line_split[0], 'houseInfoId': line_split[1]})

        count = 0
        with open(Constant.BASE_PATH + 'jjyWater-' + period + '_out.txt', 'w') as f:
            for sub_enter in sub_enter_group:
                house_code = self.house_info_group[sub_enter['houseInfoId']]
                if house_code in self.valid_house_info_group:
                    pass
                else:
                    count += 1
                    sql = 'delete from subscription_enter where id = ' + sub_enter['id'] + ' and period_id =' + period + ';'
                    f.write(sql + '\n')
        print(count)


if __name__ == '__main__':
    JjyWaterDeleteSubEnter().handle('70')
