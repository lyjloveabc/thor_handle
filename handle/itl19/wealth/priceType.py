from utils.file.excel.readUtil import ReadUtil

sql_house = 'UPDATE house_info SET price_type_name = "{price_type_name}" WHERE zone_id = {zone_id} AND id = {id};'
sql_store = 'UPDATE itl_store SET price_type_name = "{price_type_name}" WHERE zone_id = {zone_id} AND id = {id};'
sql_parking = 'UPDATE itl_parking SET price_type_name = "{price_type_name}" WHERE zone_id = {zone_id} AND id = {id};'

file_name = 'file/住宅单价类型订正.csv'
data = ReadUtil.read_file(file_name, {'id': 0, 'zone_id': 1, 'price_type': 2})

print('数据总量：', len(data))

need = list()

for row in data:
    need.append(
        sql_house.format(price_type_name=row['price_type'], zone_id=row['zone_id'], id=row['id'])
    )

with open(file_name.replace('.', '_') + '_out.txt', 'a') as f:
    for row in need:
        f.write(row + '\n')
