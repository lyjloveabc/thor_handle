"""
景江苑-支付列表订正_20161229.xlsx
"""

from utils.ExcelReadUtil import ExcelReadUtil

__AUTHOR = 'thor'


class JjyAddTrade(object):
    __BASE_PATH = 'file/'

    def __init__(self):
        self.field_index_dict = {
            'id': 4,
            'trade_no': 2
        }
        self.payments = ExcelReadUtil.read_file(JjyAddTrade.__BASE_PATH + '帐务组合查询.xlsx', self.field_index_dict)

    def handle(self):
        for item in self.payments:
            if item['id'] != ' ':
                print('update payment set trade_no = \'' + item['trade_no'] + '\'' + ', gmt_modify = now(), remark = \'手动添加trade_no\' where id = ' + str(int(item['id'])) + ';')


if __name__ == '__main__':
    handle = JjyAddTrade()
    handle.handle()
