import re

from utils.constant.constant import Constant
from utils.file.excel.readUtil import ReadUtil


class ReadNcCar:
    def __init__(self):
        self.update_sql = 'UPDATE itl_parking SET coordinate = "{coordinate}" WHERE zone_id = 84 AND id = "{id}";'

    def handle(self, file, field_index):
        need_update = list()

        excel_data = ReadUtil.read_file(file, field_index, include_first=True)

        for ed in excel_data:
            coordinate = ReadNcCar.handle_point(ed['a']) + ';' + ReadNcCar.handle_point(ed['b']) + ';' + ReadNcCar.handle_point(ed['c']) + ';' + ReadNcCar.handle_point(ed['d'])
            need_update.append(self.update_sql.format(coordinate=coordinate, id=int(float(ed['id']))))

        with open('out.sql', 'a') as f:
            f.write(Constant.SQL_BEGIN + '\n')
            for nu in need_update:
                f.write(nu + '\n')
            f.write(Constant.SQL_COMMIT + '\n')

    @staticmethod
    def handle_point(source):
        s = str(int(float(source)))
        s_group = re.search(r'(\d+)(\d{3})', s)
        return s_group.group(1) + ',' + s_group.group(2)


if __name__ == '__main__':
    bill_handle = ReadNcCar()
    bill_handle.handle(
        '南城坐标2222.xlsx',
        {
            'id': 0,
            'name': 1,
            'a': 2,
            'b': 3,
            'c': 4,
            'd': 5,
        }
    )
