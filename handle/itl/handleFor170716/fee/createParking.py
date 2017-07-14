"""
处理菜单
"""
from handle.itl.handleFor170716.dbUtil import DbUtil


class CreateParking:
    def __init__(self, *args, **kw):
        self.dbUtil = kw['dbUtil']

    def handle(self):
        self._product_type()
        self._product()
        # self._subscription()

    def _product_type(self):
        sql_define = ["INSERT INTO product_type (id, name, bill_name, code, icon, gmt_create, gmt_modify, description, status)"
                      "VALUES(27, '车位费', '车位费', 'parking', 'producttype/170406/1491477935.png', now(), now(), '', 'VALID');"]
        self.dbUtil.out_sql(sql_define, '添加车位费product_type')
        self.dbUtil.exe_on_db(sql_define)

    def _product(self):
        sql_define = ["INSERT INTO product (id, name, product_type_id, product_type_code, period, gmt_create, gmt_modify,"
                      "fee_rule, status)"
                      "VALUES(16, '车位费', 27, 'parking', 'month', now(), now(), "
                      "'{\"type\":\"common\",\"UnitAmounts\":[{\"dosage\":0,\"unitAmount\":1.95}],\"feeRule\":\"count * unitPrice\"}', 'VALID');"]
        self.dbUtil.out_sql(sql_define, '添加车位费product')
        self.dbUtil.exe_on_db(sql_define)

    def _subscription(self):
        sql_define = ["INSERT INTO subscription (name, product_id, zone_id, gmt_create, gmt_modify, num,"
                      "total_amount, status, year_start_month)"
                      "VALUES('翡翠城车位费', 16, 1, now(), now(), 0, 0.00, "
                      "'VALID', '01');"]
        self.dbUtil.out_sql(sql_define, '翡翠城订阅车位费')
        self.dbUtil.exe_on_db(sql_define)


if __name__ == '__main__':
    handle = CreateParking(**{'dbUtil': DbUtil()})
    handle.handle()
