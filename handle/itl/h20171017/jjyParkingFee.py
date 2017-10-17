from utils.db.daoUtil import DaoUtils
from utils.db.mysql.mySQLConfig import MySQLConfig
from utils.file.excel.readUtil import ReadUtil


class JjyParkingFee:
    def __init__(self):
        # bill itl_parking_bill itl_parking
        self.dao = DaoUtils(**{'dbType': 'MySQL', 'config': MySQLConfig.localhost()})

        self.field_index = {
            'parking_name': 0,
            'end_time': 1,
        }

        self.select_sql = 'SELECT itl_parking_bill.bill_id AS bill_id' \
                          ' FROM itl_parking_bill' \
                          ' LEFT JOIN itl_parking ON itl_parking.id = itl_parking_bill.parking_id' \
                          ' LEFT JOIN bill ON bill.id = itl_parking_bill.bill_id' \
                          ' WHERE itl_parking.zone_id = 2 AND itl_parking.name = "{parking_name}" AND CAST(date_format(bill.gmt_start, \'%Y%m\') AS SIGNED) <= {day};'

        self.update_sql = 'UPDATE bill SET' \
                          ' real_amount = financial_income, gmt_modify = now(), gmt_pay = now(), remark = \'车位收费上线之前，已线下收费，没有支付流水\',' \
                          ' status = \'PAID\', financial_income = 0.00 where id = {bill_id};'

    def handle(self, money_file):
        bill_ids = list()
        data = ReadUtil.read_file(money_file, self.field_index)

        for row in data:
            end_time = str(row['end_time'])
            if end_time is not None and end_time != '':
                day_split = str(row['end_time']).split('/')

                sql = self.select_sql.format(parking_name=row['parking_name'], day=day_split[0].zfill(4) + day_split[1].zfill(2))
                row_data = self.dao.get_all(sql)
                for temp in row_data:
                    bill_ids.append(temp['bill_id'])
            else:
                pass

        with open('out.sql', 'a') as f:
            for row in bill_ids:
                f.write(self.update_sql.format(bill_id=row))
                f.write('\n')


if __name__ == '__main__':
    jjy = JjyParkingFee()
    jjy.handle('file/money1017.xlsx')
