from utils.constant.constant import Constant
from utils.db.daoUtil import DaoUtils
from utils.db.mysql.mySQLConfig import MySQLConfig


class PaymentSub:
    def __init__(self):
        self.dao = DaoUtils(**{'dbType': 'MySQL', 'config': MySQLConfig.localhost()})
        self.sql = 'INSERT ignore INTO itl_payment_sub' \
                   '(created_time, modified_time, payment_id, product_type_code, bill_id, actual_amount) VALUES (now(),now(),{p}, "{c}", {b}, "{a}");'

    def handle(self):
        payment_list = self.dao.get_all('SELECT id, type, bill_ids, pay_amount FROM payment WHERE status = "PAID" AND type IS NOT NULL;')
        bill_list = self.dao.get_all('SELECT id, payment_id, real_amount FROM bill;')
        bill_map = dict()

        for bill in bill_list:
            bill_map[bill['id']] = bill['real_amount']

        with open('out_PaymentSub.sql', 'a') as f:
            f.write(Constant.SQL_BEGIN)
            for payment in payment_list:
                if payment['bill_ids'] is None or payment['bill_ids'] == '':
                    f.write(
                        self.sql.format(p=payment['id'], c=payment['type'], b='null', a=payment['pay_amount']) + '\n'
                    )
                else:
                    bill_id_list = str(payment['bill_ids']).split(',')
                    for bill_id in bill_id_list:
                        if int(bill_id) in bill_map:
                            f.write(
                                self.sql.format(p=payment['id'], c=payment['type'], b=bill_id, a=bill_map[int(bill_id)]) + '\n'
                            )
            f.write(Constant.SQL_COMMIT)


if __name__ == '__main__':
    pay = PaymentSub()
    pay.handle()
