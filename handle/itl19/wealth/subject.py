sql = 'INSERT INTO itl_finance_subject(id, gmt_create, gmt_modified, name, icon, is_put_bill, sort_num) ' \
      'VALUES ({id}, now(), now(), "{name}", "{icon}", 0, {sort_num});'

index = 1
with open('file/product_type.txt', 'r') as f:
    for line in f.readlines():
        line = line.replace('\n', '')
        d_a = line.split(',')
        print(sql.format(id=d_a[0], name=d_a[1], icon=d_a[2] if len(d_a) > 2 else '', sort_num=index))
        index += 1
