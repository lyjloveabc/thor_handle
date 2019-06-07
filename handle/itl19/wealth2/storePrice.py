from utils.file.excel.readUtil import ReadUtil

file_name = 'file/itl_store表修改.xlsx'
data = ReadUtil.read_file(file_name, {'id': 0, 'price': 2})

sql = 'UPDATE itl_store SET price_type_name = "{price_type_name}" WHERE id = {id};'

with open(file_name + '.txt', 'a') as f:
    for row in data:
        f.write(
            sql.format(price_type_name=row['price'], id=row['id']) + '\n'
        )
