from utils.db.daoUtil import DaoUtils
from utils.db.mysql.mySQLConfig import MySQLConfig
from utils.file.excel.readUtil import ReadUtil


class JjyParkingFee20171022:
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

        self.select_sql = 'SELECT itl_parking_bill.bill_id AS bill_id, bill.house_info_id AS house_info_id, itl_parking.name AS parking_name, bill.remark AS remark, bill.gmt_start AS start' \
                          ' FROM itl_parking_bill' \
                          ' LEFT JOIN itl_parking ON itl_parking.id = itl_parking_bill.parking_id' \
                          ' LEFT JOIN bill ON bill.id = itl_parking_bill.bill_id' \
                          ' WHERE itl_parking.zone_id = 2 AND itl_parking.name = "{parking_name}"' \
                          ' AND payment_ids !=\'\';'

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
                    bill_ids.append(
                        {
                            'id': temp['bill_id'],
                            'house_info_id': temp['house_info_id'],
                            'parking_name': temp['parking_name'],
                            'remark': temp['remark'],
                            'start': temp['start'],
                        }
                    )

        print(len(bill_ids))
        for row in bill_ids:
            print(row)


if __name__ == '__main__':
    jjy = JjyParkingFee20171022()
    jjy.handle('file/需要订正的数据.xlsx')
