from utils.constant.constant import Constant
from utils.db.daoUtil import DaoUtils
from utils.db.mysql.mySQLConfig import MySQLConfig
from utils.file.excel.readUtil import ReadUtil


class WycHistoricalFee:
    def __init__(self):
        self.dao = DaoUtils(**{'dbType': 'MySQL', 'config': MySQLConfig.localhost()})

        self.delete_bill_sql = 'DELETE FROM bill WHERE zone_id = 24 AND product_type_code = "propertyFee" AND house_info_id = {house_info_id} AND id != 10792 AND id != 10829;'

        self.delete_sub_enter_sql = 'DELETE FROM subscription_enter WHERE zone_id = 24 AND product_type_code = "propertyFee" AND house_info_id = {house_info_id};'

        self.update_sql = 'UPDATE bill SET title="{title}", ought_amount={ought_amount}, gmt_modify=now(), remark="{remark}", is_checked=1,' \
                          ' financial_income="{financial_income}" WHERE zone_id = 24 AND product_type_code = "propertyFee" AND house_info_id = {house_info_id};'

    def handle(self, file, field_index):
        db_house_dict = dict()  # key-房id，value-房code
        file_house_codes = set()  # 待处理文件中已存在的房号code

        base = ReadUtil.read_file(file, field_index)  # 待处理的数据
        houses = self.dao.get_all('SELECT id, code FROM house_info WHERE zone_id = 24;')  # 万源城逸郡所有的房号

        for house in houses:
            db_house_dict[str(house['code'])] = house['id']

        for b in base:
            file_house_codes.add(str(b['house_code']))

        with open('out_wyc.sql', 'a') as f:
            f.write(Constant.SQL_BEGIN + '\n')
            for key in db_house_dict.keys():
                if key not in file_house_codes:
                    f.write(self.delete_bill_sql.format(house_info_id=db_house_dict[key]) + '\n')
                    f.write(self.delete_sub_enter_sql.format(house_info_id=db_house_dict[key]) + '\n')

        with open('out_wyc.sql', 'a') as f:
            for row in base:
                f.write(
                    self.update_sql.format(
                        title=row['bill_tile'],
                        ought_amount=row['money'],
                        remark='历史遗留账单处理',
                        financial_income=row['money'],
                        house_info_id=db_house_dict[row['house_code']]
                    )
                    + '\n'
                )
            f.write(Constant.SQL_COMMIT + '\n')


if __name__ == '__main__':
    obj = WycHistoricalFee()
    obj.handle(
        'file/万源城逸郡账单.xlsx',
        {
            'house_code': 0,
            'bill_tile': 3,
            'money': 4,
        }
    )
