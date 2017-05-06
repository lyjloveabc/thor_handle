"""
景江苑-支付列表订正_20161229.xlsx
"""

from utils.ExcelReadUtil import ExcelReadUtil

__AUTHOR = 'thor'


class BillStatusFix(object):
    __BASE_PATH = 'file/'

    def __init__(self):
        self.field_index_dict = {
            'status': 1,
            'id': 2
        }
        self.no_confirm = ExcelReadUtil.read_file(BillStatusFix.__BASE_PATH + '未确认账单from云霄.xls', self.field_index_dict)

    def handle(self):
        for item in self.no_confirm:
            id = item['id']
            if item['status'] == '未交':
                sql = 'update bill set payment_id = null, gmt_modify = now(), gmt_pay = null, remark = "未确认修改成未支付", status = "NO_PAY" where id = {id};' \
                    .format(id=id)
            elif item['status'] == '无此房号':
                sql = 'delete from bill where id = {id};'.format(id=id)
            elif item['status'] == '3月4日现金交':
                pass
            elif item['status'] == '':
                pass
            print(sql)


if __name__ == '__main__':
    handle = BillStatusFix()
    handle.handle()
# 景江苑 52



# update bill set payment_id = null, real_amount = null, gmt_modify = now(),
# remark = '手动修改为NO_PAY', status = 'NO_PAY'
# where id in (
# 255,
# 427,
# 1135,
# 1307,
# 1310,
# 1480,
# 1518,
# 1597,
# 1615,
# 1769,
# 1772,
# 1942,
# 2059,
# 2077,
# 2231,
# 2233,
# 2234);
