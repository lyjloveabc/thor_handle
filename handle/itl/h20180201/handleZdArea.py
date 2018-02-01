from utils.constant.constant import Constant
from utils.file.excel.readUtil import ReadUtil


class HandleZdArea:
    def __init__(self):
        self.sql = 'UPDATE house_info SET area = "{area}", uname = "{un}", mobile="{m}", notice="阿苏->罗宣修改" WHERE id = {id} and zone_id = 82;'

    def handle(self):
        field_index = {
            'house': 0,
            'building': 1,
            'door': 2,
            'area': 3,
            'name': 4,
            'mobile': 5,
        }
        rows = ReadUtil.read_file('浙地面积修改.xlsx', field_index)

        dbs = dict()

        with open('zd.txt', 'r') as f:
            for line in f.readlines():
                arr = line.replace('\n', '').split(',')
                key = str(int(arr[1])) + '-' + str(int(arr[2])) + '-' + str(int(arr[3]))
                dbs[key] = str(int(arr[0]))

        result = list()

        for row in rows:
            key = row['house'] + '-' + row['building'] + '-' + row['door']
            if key in dbs:
                result.append(self.sql.format(area=row['area'], un=row['name'], m=row['mobile'], id=dbs[key]))
            else:
                print('not in dbs key: ', key)

        with open('out.sql', 'a') as f:
            f.write(Constant.SQL_BEGIN + '\n')
            for row in result:
                f.write(row + '\n')
            f.write(Constant.SQL_COMMIT + '\n')


if __name__ == '__main__':
    o = HandleZdArea()
    o.handle()
