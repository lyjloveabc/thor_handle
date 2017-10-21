from utils.db.daoUtil import DaoUtils
from utils.db.mysql.mySQLConfig import MySQLConfig
from utils.file.excel.readUtil import ReadUtil


class JjyParkingFee20171022:
    def __init__(self):
        # bill itl_parking_bill itl_parking
        self.dao = DaoUtils(**{'dbType': 'MySQL', 'config': MySQLConfig.localhost()})

        self.data = dict()

        self.field_index = {
            'parking_name': 0,
            'end_time': 1,
        }

        self.field_index_special = {
            'parking_name': 0,
            'end_time': 1,
            'need_pad': 8,
        }

        self.select_sql = 'SELECT itl_parking_bill.bill_id AS bill_id' \
                          ' FROM itl_parking_bill' \
                          ' LEFT JOIN itl_parking ON itl_parking.id = itl_parking_bill.parking_id' \
                          ' LEFT JOIN bill ON bill.id = itl_parking_bill.bill_id' \
                          ' WHERE itl_parking.zone_id = 2 AND itl_parking.name = "{parking_name}" AND CAST(date_format(bill.gmt_start, \'%Y%m\') AS SIGNED) < {day_data}' \
                          ' AND payment_ids =\'\';'

        self.update_sql = 'UPDATE bill SET' \
                          ' real_amount = ought_amount, gmt_modify = now(), gmt_pay = now(), remark = \'[第二批系统处理]车位收费上线之前，已线下收费，没有支付流水\',' \
                          ' status = \'PAID\', financial_income = 0.00 WHERE id = {bill_id};'

        self.select_sql_special = 'SELECT itl_parking_bill.bill_id AS bill_id' \
                                  ' FROM itl_parking_bill' \
                                  ' LEFT JOIN itl_parking ON itl_parking.id = itl_parking_bill.parking_id' \
                                  ' LEFT JOIN bill ON bill.id = itl_parking_bill.bill_id' \
                                  ' WHERE itl_parking.zone_id = 2 AND itl_parking.name = "{parking_name}" AND CAST(date_format(bill.gmt_start, \'%Y%m\') AS SIGNED) = {day_data}' \
                                  ' AND payment_ids =\'\';'

        self.update_sql_special = 'UPDATE bill SET ' \
                                  '  real_amount = ought_amount - {need_pay}, gmt_modify = now(), gmt_pay = now(), is_part_paid = 1,' \
                                  ' remark = \'[第二批系统处理]车位收费上线之前，已线下收费[当前特殊月处理]，没有支付流水\', STATUS = \'NO_PAY\', financial_income = {need_pay}' \
                                  ' WHERE id = {bill_id};'

        self.select_dy_sql = 'SELECT itl_parking_bill.bill_id AS bill_id' \
                             ' FROM itl_parking_bill' \
                             ' LEFT JOIN itl_parking ON itl_parking.id = itl_parking_bill.parking_id' \
                             ' LEFT JOIN bill ON bill.id = itl_parking_bill.bill_id' \
                             ' WHERE itl_parking.zone_id = 2 AND itl_parking.name = "{parking_name}" AND CAST(date_format(bill.gmt_start, \'%Y%m\') AS SIGNED) > {day_data}' \
                             ' AND payment_ids =\'\' AND status != \'NO_PAY\';'

        self.update_dy_sql = 'UPDATE bill SET' \
                             ' real_amount = NULL , gmt_modify = now(), gmt_pay = NULL , financial_income = ought_amount, ' \
                             ' remark = \'[第二批系统处理]车位收费上线之前，没有付款\',' \
                             ' status = \'NO_PAY\' WHERE id = {bill_id};'

    def handle(self, money_file):
        bill_ids = list()
        data = ReadUtil.read_file(money_file, self.field_index)

        for row in data:
            end_time = str(row['end_time'])
            if end_time is not None and end_time != '':
                day_split = str(row['end_time']).split('/')

                sql = self.select_sql.format(parking_name=row['parking_name'], day_data=day_split[0].zfill(4) + day_split[1].zfill(2))
                row_data = self.dao.get_all(sql)
                for temp in row_data:
                    bill_ids.append(temp['bill_id'])
                self.data[row['parking_name']] = (self.data[row['parking_name']] + len(row_data)) if row['parking_name'] in self.data else len(row_data)
            else:
                pass

        with open('out_第二批.sql', 'a') as f:
            for row in bill_ids:
                f.write(self.update_sql.format(bill_id=row))
                f.write('\n')

    def handle_special(self, money_file):
        bill_ids = list()
        data = ReadUtil.read_file(money_file, self.field_index_special)

        for row in data:
            end_time = str(row['end_time'])
            if end_time is not None and end_time != '' and round(float(row['need_pad']), 2) > 0:
                day_split = str(row['end_time']).split('/')

                sql = self.select_sql_special.format(parking_name=row['parking_name'], day_data=day_split[0].zfill(4) + day_split[1].zfill(2))
                row_data = self.dao.get_all(sql)
                for temp in row_data:
                    bill_ids.append(
                        {
                            'bill_id': temp['bill_id'],
                            'need_pad': round(float(row['need_pad']), 2),
                        }
                    )
                self.data[row['parking_name']] = (self.data[row['parking_name']] + len(row_data)) if row['parking_name'] in self.data else len(row_data)

        with open('out_special_第二批.sql', 'a') as f:
            for row in bill_ids:
                f.write(self.update_sql_special.format(need_pay=row['need_pad'], bill_id=row['bill_id']))
                f.write('\n')

    def handle_dy(self, money_file):
        bill_ids = list()
        data = ReadUtil.read_file(money_file, self.field_index)

        for row in data:
            end_time = str(row['end_time'])
            if end_time is not None and end_time != '':
                day_split = str(row['end_time']).split('/')

                sql = self.select_dy_sql.format(parking_name=row['parking_name'], day_data=day_split[0].zfill(4) + day_split[1].zfill(2))
                row_data = self.dao.get_all(sql)
                for temp in row_data:
                    bill_ids.append(temp['bill_id'])
                self.data[row['parking_name']] = (self.data[row['parking_name']] + len(row_data)) if row['parking_name'] in self.data else len(row_data)

        with open('out_第二批_dy.sql', 'a') as f:
            for row in bill_ids:
                f.write(self.update_dy_sql.format(bill_id=row))
                f.write('\n')


if __name__ == '__main__':
    jjy = JjyParkingFee20171022()
    jjy.handle('file/需要订正的数据.xlsx')
    jjy.handle_special('file/需要订正的数据.xlsx')
    jjy.handle_dy('file/需要订正的数据.xlsx')
    for key in jjy.data.keys():
        print(str(key) + '     ' + str(jjy.data[key]))
