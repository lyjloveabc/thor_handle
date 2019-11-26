sql_base = "insert into baseshop (code, name, province_code, city_code, region_code, place, is_test)" \
           " values ('{code}', '{name}', '{province_code}', '{city_code}', '{region_code}', '{place}', '{is_test}');"
sql_list = list()

with open('long_text_2019-11-19-14-33-56.txt', 'r') as f:
    for row in f.readlines():
        row = row.replace('\n', '')
        data = row.split(',')
        sql_list.append(
            sql_base.format(
                code=data[0],
                name=data[1],
                province_code=data[2],
                city_code=data[3],
                region_code=data[4],
                place=data[5],
                is_test=data[6],
            )
        )

with open('long_text_2019-11-19-14-33-56_out.txt', 'a') as f:
    for row in sql_list:
        f.write(row + '\n')

