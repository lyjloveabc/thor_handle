from utils.db.daoUtil import DaoUtils
from utils.db.mysql.mySQLConfig import MySQLConfig


class PaymentSub:
    def __init__(self):
        self.dao = DaoUtils(**{'dbType': 'MySQL', 'config': MySQLConfig.localhost()})

    def handle(self):
        self.dao.get_all('select payment')


if __name__ == '__main__':
    pay = PaymentSub()
    pay.handle()
