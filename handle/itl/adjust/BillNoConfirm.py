# encoding=utf-8
"""
景江苑账单隐藏
"""

__AUTHOR = 'thor'

class BillNoConfirm(object):
    __BASE_PATH = 'file/'

    def __init__(self):
        self.field_index_dict = {
            'house_code': 0,
            'september_num': 1,
            'october_num': 2,
        }

    def handle(self):
        per_sql = 'update bill set status = \'NO_CONFIRM\' where house_info_id in ('
        print(per_sql, end='')

        with open(BillNoConfirm.__BASE_PATH + 'houseId.txt', 'r') as f:
            for line in f.readlines():
                print(line[:-1] + ', ', end='')
        print(');')

    @staticmethod
    def to4(temp):
        if len(temp) == 3:
            temp = '0' + temp
        return temp


if __name__ == '__main__':
    handle = BillNoConfirm()
    handle.handle()

# select * from bill where house_info_id in
# (17, 462, 94, 302, 95, 109, 123, 137, 233, 246, 259, 272, 3137,
# 151, 167, 199, 216, 203, 204, 221, 3138, 313, 331, 330, 348, 349, 367, 35);

#update bill set status = 'NO_CONFIRM' where house_info_id in (17, 94, 302, 95, 109, 123, 137, 233, 246, 259, 272, 151, 167, 199, 216, 203, 204, 221, 313, 331, 330, 348, 349, 367, 35);

# update bill set status = 'NO_CONFIRM'
# where house_info_id in
# (17, 94, 302, 95, 109, 123, 137, 233, 246, 259, 272, 151, 167, 199, 216, 203, 204, 221, 313, 331, 330, 348, 349, 367, 35)
# and product_type_code = 'propertyFee';

