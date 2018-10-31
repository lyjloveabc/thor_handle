sql = 'UPDATE house_info SET commercial_kind = "海军" WHERE zone_id = 2 AND house = {house} AND building = {building} AND door= {door};'

sql_2 = 'UPDATE house_info SET commercial_kind = "海军" WHERE zone_id = 2 AND house = {house};'

with open('house.txt', 'r') as f:
    for row in f.readlines():
        row = row.replace('\n', '').replace('幢', ',').replace('单元', ',')
        data = row.split(',')
        print(sql.format(house=data[0], building=data[1], door=data[2]))

print(sql_2.format(house=11))
print(sql_2.format(house=12))
