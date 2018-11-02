# sql = 'UPDATE house_info SET commercial_kind = "海军" WHERE zone_id = 2 AND house = {house} AND building = {building} AND door= {door};'
#
# sql_2 = 'UPDATE house_info SET commercial_kind = "海军" WHERE zone_id = 2 AND house = {house};'
#
# with open('house.txt', 'r') as f:
#     for row in f.readlines():
#         row = row.replace('\n', '').replace('幢', ',').replace('单元', ',')
#         data = row.split(',')
#         print(sql.format(house=data[0], building=data[1], door=data[2]))
#
# print(sql_2.format(house=11))
# print(sql_2.format(house=12))

#

m1 = '(house = {house} AND building = {building} AND door= {door}) or '
m2 = '(house = {house}) or '

# b_sql = 'SELECT * FROM bill WHERE zone_id = 2 AND house = {house} AND building = {building} AND door= {door};'
b_sql = 'SELECT * FROM bill WHERE zone_id = 2 AND house_info_id in ( '

with open('house.txt', 'r') as f:
    for row in f.readlines():
        row = row.replace('\n', '').replace('幢', ',').replace('单元', ',')
        data = row.split(',')

        b_sql += m1.format(house=data[0], building=data[1], door=data[2])

b_sql += m2.format(house=11)
b_sql += m2.format(house=12)
print(b_sql)
