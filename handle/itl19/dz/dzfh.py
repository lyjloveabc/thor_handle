from utils.file.excel.readUtil import ReadUtil

sql_update = 'UPDATE house_info SET name = "{name}", price_type_name = "{price_type_name}" WHERE zone_id = 135 AND id ={id};'
data = ReadUtil.read_file('file/蓝庭房号数据订正.xlsx', {
    'id': 0,
    'name': 1,
    'price_type_name': 2,
})

for row in data:
    print(sql_update.format(id=row['id'], name=row['name'], price_type_name=row['price_type_name']))
