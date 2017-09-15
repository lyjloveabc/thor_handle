from utils.constant.constant import Constant
from utils.file.excel.readUtil import ReadUtil


class ImportParking:
    def __init__(self):
        self.field_index = {
            'name1': 0,
            'name2': 1,
            'point1': 2,
            'point2': 3,
            'point3': 4,
            'point4': 5,
            'type': 6,
        }
        self.base_sql = 'INSERT INTO itl_parking ' \
                        '(created_time, modified_time, zone_id, name, owner_type, contact, contact_mobile, coordinate, last_operator)' \
                        'VALUES (now(), now(), 1, "{name}", "{owner_type}", "", "", "{coordinate}", 431);'
        self.base_update_sql = 'UPDATE itl_parking ' \
                               'SET modified_time = now(), coordinate = "{coordinate}" WHERE zone_id= "{zone_id}" AND name = "{name}";'

    def handle(self, file_name):
        result_list = ReadUtil.read_file(file_name, self.field_index, True)
        print('len: ' + str(len(result_list)))

        print(Constant.SQL_BEGIN)
        for row in result_list:
            print(self.base_sql.format(name=row['name1'] + '-' + row['name2'], owner_type=row['type'],
                                       coordinate=row['point1'] + ';' + row['point2'] + ';' + row['point3'] + ';' + row['point4'] + ''))
        print(Constant.SQL_BEGIN)

        print()

        print(Constant.SQL_BEGIN)
        for row in result_list:
            print(self.base_update_sql.format(coordinate=row['point1'] + ';' + row['point2'] + ';' + row['point3'] + ';' + row['point4'] + '',
                                              zone_id=1, name=row['name1'] + '-' + row['name2']))
        print(Constant.SQL_BEGIN)


if __name__ == '__main__':
    obj = ImportParking()
    obj.handle("file/车位整理0915OK.xlsx")
