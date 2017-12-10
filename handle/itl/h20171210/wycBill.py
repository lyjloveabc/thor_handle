from utils.constant.constant import Constant
from utils.db.daoUtil import DaoUtils
from utils.db.mysql.mySQLConfig import MySQLConfig
from utils.file.excel.readUtil import ReadUtil


class WycBill:
    def __init__(self):
        self.dao = DaoUtils(**{'dbType': 'MySQL', 'config': MySQLConfig.localhost()})

        self.day_title = {
            '2018-01-01': '物业费+车位管理费2018年01月-03月',
            '2018-04-01': '物业费+车位管理费2018年04月-06月',
            '2018-07-01': '物业费+车位管理费2018年07月-09月',
            '2018-10-01': '物业费+车位管理费2018年10月-12月',
        }

        self.sql = 'SELECT bill.id, CONCAT( house_info.house, "-", house_info.building, "-", CAST(house_info.door AS SIGNED)) AS k, gmt_start AS s' \
                   ' FROM bill LEFT JOIN house_info ON house_info.id = bill.house_info_id' \
                   ' WHERE bill.zone_id = 24 AND product_type_id = 7 AND gmt_start IN ("2018-01-01", "2018-04-01", "2018-07-01", "2018-10-01");'

        self.sql_update = 'UPDATE bill SET title = "{title}", ought_amount = {money}, gmt_modify = now(), remark = "手动更改", financial_income = {money} WHERE id = {id};'

    def handle(self, file, field_index):
        need_update = list()

        excel_data = ReadUtil.read_file(file, field_index)

        bill_db = self.dao.get_all(self.sql)

        for ed in excel_data:
            key = ed['house'] + '-' + ed['building'] + '-' + ed['door']
            for bill in bill_db:
                if key == bill['k']:
                    need_update.append(
                        self.sql_update.format(title=self.day_title[str(bill['s'])], money=ed[str(bill['s'])], id=bill['id'])
                    )

        with open('out.sql', 'a') as f:
            f.write(Constant.SQL_BEGIN + '\n')
            for nu in need_update:
                f.write(nu + '\n')
            f.write(Constant.SQL_COMMIT + '\n')


if __name__ == '__main__':
    bill_handle = WycBill()
    bill_handle.handle(
        '万源城的数据调整-to小罗.xlsx',
        {
            'house': 0,
            'building': 1,
            'door': 2,
            '2018-01-01': 3,
            '2018-04-01': 4,
            '2018-07-01': 5,
            '2018-10-01': 6,
        }
    )
