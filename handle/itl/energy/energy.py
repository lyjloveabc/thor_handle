from utils.constant.constant import Constant
from utils.file.excel.readUtil import ReadUtil

# 插入的sql模板
sql = 'INSERT INTO itl_energy_table(gmt_create, gmt_modified, zone_id, energy_table_kind, is_stopped,' \
      'name, type, estate, estate_id, estate_name, base, creator_id, last, last_time, last_person) VALUES ' \
      '(now(), now(), "{zone_id}", "{energy_table_kind}", 0, "{name}", "{type}", "{estate}", ' \
      '"{estate_id}", "{estate_name}", "{base}", "{creator_id}", "{last}", now(), "{last_person}");'

# 表类型：ELECTRIC-电表、WATER-水表
kind = {
    '电表': 'ELECTRIC',
    '水表': 'WATER'
}

# 不动产类型：HOUSE-住宅、STORE-商铺、SHOP-店铺、OTHER-其他
estate = {
    '住宅': 'HOUSE',
    '商铺': 'STORE',
    '店铺': 'SHOP',
    '其他': 'OTHER',
}

# 房号数据
house = dict()
house_file = 'jjyhouse_20180925.txt'
with open(house_file, 'r') as f:
    for row in f.readlines():
        row = row.replace('\n', '')
        data = row.split(',')
        house[int(data[0])] = str(data[1]) + '幢' + str(data[2]) + '单元' + str(data[3]) + '室'

# 店铺数据
shop = dict()
shop_file = 'jjyshop_20180925.txt'
with open(shop_file, 'r') as f:
    for row in f.readlines():
        row = row.replace('\n', '')
        data = row.split(',')
        shop[int(data[0])] = str(data[1])

field_index = {
    'kind': 0,
    'created_time': 1,
    'zone': 2,
    'name': 3,
    'type': 4,
    'house': 5,
    'en': 6,
    'base': 7,
}

file_name = '数据订正.xlsx'
data = ReadUtil.read_file(file_name, field_index)

with open('out.sql', 'w') as f:
    f.write(Constant.SQL_BEGIN + '\n')
    for row in data:
        print(row)
        name = ''
        energy_table_kind = kind[row['kind']]
        if row['name'] == '根据房号id取房号名':
            name = house[int(float(row['house']))]
        elif row['name'] == '根据id取店铺名':
            name = shop[int(float(row['house']))]
        else:
            name = row['name']
        f.write(
            sql.format(
                zone_id=row['zone'], energy_table_kind=energy_table_kind, name=name, type='PRIVATE', estate=estate[row['type']], estate_id=row['house'],
                estate_name=name, base=row['base'], creator_id=399, last=row['base'], last_person=399
            ) + '\n'
        )
    f.write(Constant.SQL_COMMIT + '\n')
