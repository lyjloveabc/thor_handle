import os

# code,name,province_code,city_code,region_code,place,is_test

file_name = ''
source_shop = list()

with open(file_name, 'r') as f:
    for row in f.readlines():
        row = row.replace('\n', '')
        data = row.split(',')
        source_shop.append(
            {
                'code': data[0],
                'name': data[1],
                'province_code': data[2],
                'city_code': data[3],
                'region_code': data[4],
                'place': data[5],
                'is_test': data[6],
            }
        )

# baseshop 表处理
baseshop_sql = "insert ignore into baseshop (code, name, province_code, city_code, region_code, place, is_test)" \
               " values ('{code}', '{name}', '{province_code}', '{city_code}', '{region_code}', '{place}', '{is_test}');"
out_baseshop = 'out_' + file_name

if os.path.exists(out_baseshop):
    os.remove(out_baseshop)

with open(out_baseshop, 'a') as f:
    for row in source_shop:
        f.write(baseshop_sql.format(
            code=row['row'],
            name=row['name'],
            province_code=row['province_code'],
            city_code=row['city_code'],
            region_code=row['region_code'],
            place=row['place'],
            is_test=row['is_test'],
        ) + '\n')

# authshop_new 表处理
auth_sql = "insert into authshop_new (code) values ('{code}');"
out_auth = 'out_auth_' + file_name

if os.path.exists(out_auth):
    os.remove(out_auth)

with open(out_auth, 'a') as f:
    for row in source_shop:
        f.write(auth_sql.format(
            code=row['row']
        ) + '\n')
