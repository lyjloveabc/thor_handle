sql = 'INSERT INTO `itl_finance_flexible_pay`(zone_id) VALUES ({zone_id});'

with open('1.txt', 'r') as f:
    index = 0
    for row in f.readlines():
        print(sql.format(zone_id=row.replace('\n', '')))
        index += 1
    print(index)
