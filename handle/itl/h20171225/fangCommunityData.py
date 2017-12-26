sql = "INSERT INTO g15_open_province (created_time, modified_time, province_name, status, opened_time) VALUES (now(), now(), '{province_name}', 'LATER', NULL);"

with open('province.txt', 'r') as f:
    for row in f.readlines():
        print(sql.format(province_name=row.replace('\n', '')))
