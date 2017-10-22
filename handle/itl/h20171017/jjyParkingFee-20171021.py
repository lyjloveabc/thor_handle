from utils.db.daoUtil import DaoUtils
from utils.db.mysql.mySQLConfig import MySQLConfig
from utils.file.excel.readUtil import ReadUtil


class JjyParkingFee20171021:
    def __init__(self):
        self.dao = DaoUtils(**{'dbType': 'MySQL', 'config': MySQLConfig.localhost()})

        self.field_index = {
            'parking_name': 0,
            'end_time': 1,
        }

        self.field_index_special = {
            'parking_name': 0,
            'end_time': 1,
            'need_pad': 8,
        }

        self.select_sql = 'SELECT itl_parking_bill.bill_id AS bill_id, itl_parking.name AS pn, itl_parking.house_info_id AS house, bill.title AS bt' \
                          ' FROM itl_parking_bill' \
                          ' LEFT JOIN itl_parking ON itl_parking.id = itl_parking_bill.parking_id' \
                          ' LEFT JOIN bill ON bill.id = itl_parking_bill.bill_id' \
                          ' WHERE itl_parking.zone_id = 2 AND itl_parking.name = "{parking_name}" AND CAST(date_format(bill.gmt_start, \'%Y%m\') AS SIGNED) = {day_data}' \
                          ' AND payment_ids =\'\';'

        self.update_sql = 'UPDATE bill SET ' \
                          ' real_amount = ought_amount, gmt_modify = now(), gmt_pay = now(),' \
                          ' remark = \'[第3批系统处理]车位收费上线之前，已线下收费[当前特殊月处理]，没有支付流水\', STATUS = \'PAID\', financial_income = 0.00' \
                          ' WHERE id = {bill_id};'

    def handle(self, money_file):
        bill_ids = list()
        data = ReadUtil.read_file(money_file, self.field_index_special)

        for row in data:
            end_time = str(row['end_time'])
            if end_time is not None and end_time != '' and round(float(row['need_pad']), 2) == 0:
                day_split = str(row['end_time']).split('/')

                sql = self.select_sql.format(parking_name=row['parking_name'], day_data=day_split[0].zfill(4) + day_split[1].zfill(2))
                row_data = self.dao.get_all(sql)
                for temp in row_data:
                    bill_ids.append(
                        {
                            'billId': temp['bill_id'],
                            'parkingName': temp['pn'],
                            'house_id': temp['house'],
                            'bill_name': temp['bt'],
                        }
                    )
        return bill_ids
        # bill_ids.append(temp['bill_id'])
        # with open('out_第3批.sql', 'a') as f:
        #     for row in bill_ids:
        #         f.write(self.update_sql.format(bill_id=row))
        #         f.write('\n')

        # return bill_ids


if __name__ == '__main__':
    jjy = JjyParkingFee20171021()
    # jjy.handle('file/需要订正的数据.xlsx')
    ad = jjy.handle('file/需要订正的数据.xlsx')
    for temp in ad:
        print(temp)
