sql_base = "update baseshop set is_test = 100 where code = '{code}';"
sql_list = list()

with open('long_text_2019-11-19-14-33-56.txt', 'r') as f:
    for row in f.readlines():
        row = row.replace('\n', '')
        data = row.split(',')
        sql_list.append(
            sql_base.format(
                code=data[0]
            )
        )

with open('long_text_2019-11-19-14-33-56_out_update.txt', 'a') as f:
    for row in sql_list:
        f.write(row + '\n')
