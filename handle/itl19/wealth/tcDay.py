file_name = 'file/tcBill.txt'
sql = 'UPDATE itl_finance_bill SET start_day = "{start_day}", end_day = "{end_day}" WHERE id = {id};'
need = list()
with open(file_name, 'r') as f:
    for row in f.readlines():
        row = row.replace('\n', '')
        row = row.replace('/', '-')
        temp = row.split('	')
        need.append({
            'id': temp[0],
            'start': temp[1],
            'end': temp[2]
        })

with open(file_name.replace('.txt', '') + '_out.txt', 'a') as f:
    for row in need:
        f.write(
            sql.format(start_day=row['start'], end_day=row['end'], id=row['id']) + '\n'
        )


file_name = 'file/tcPeriod.txt'
sql = 'UPDATE itl_finance_bill_period SET start_day = "{start_day}", end_day = "{end_day}" WHERE id = {id};'
need = list()
with open(file_name, 'r') as f:
    for row in f.readlines():
        row = row.replace('\n', '')
        row = row.replace('/', '-')
        temp = row.split('	')
        need.append({
            'id': temp[0],
            'start': temp[1],
            'end': temp[2]
        })

with open(file_name.replace('.txt', '') + '_out.txt', 'a') as f:
    for row in need:
        f.write(
            sql.format(start_day=row['start'], end_day=row['end'], id=row['id']) + '\n'
        )