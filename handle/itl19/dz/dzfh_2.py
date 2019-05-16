from utils.file.excel.readUtil import ReadUtil

sql_update = 'UPDATE house_info SET name = "{name}" WHERE id ={id};'
data = ReadUtil.read_file('file/house_info.name.xlsx', {
    'id': 0,
    'name': 1,
})

for row in data:
    print(sql_update.format(id=row['id'], name=row['name']))
