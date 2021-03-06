sql_house = 'UPDATE house_info SET price_type_name = "{price_type_name}" WHERE  id = {id};'
sql_store = 'UPDATE itl_store SET price_type_name = "{price_type_name}" WHERE  id = {id};'
sql_parking = 'UPDATE itl_parking SET price_type_name = "{price_type_name}" WHERE  id = {id};'

file_name = 'file/linshi.txt'

data = list()
with open(file_name, 'r') as f:
    for row in f.readlines():
        row = row.replace('\n', '')
        arr = row.split(' ')
        data.append({
            'id': arr[0],
            'price_type': arr[1] if len(arr) > 1 else '',
        })

print('数据总量：', len(data))

need = list()

for row in data:
    need.append(
        sql_store.format(price_type_name=row['price_type'], id=row['id'])
    )

with open(file_name.replace('.', '_') + '_out.txt', 'a') as f:
    for row in need:
        f.write(row + '\n')
