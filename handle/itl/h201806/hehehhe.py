sql = 'INSERT INTO itl_business_bill (created_time, modified_time, zone_id, business_id, bill_id, type, last_operator) ' \
      'VALUE(now(), now(), 76, {business_id}, {bill_id}, "STORE", 431);'

with open('hehehe.txt', 'r') as f:
    for row in f.readlines():
        data = row.replace('\n', '').split(',')
        print(sql.format(business_id=data[1], bill_id=data[0]))
