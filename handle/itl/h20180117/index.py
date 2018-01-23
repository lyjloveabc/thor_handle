sql = 'insert ignore into crawler_index(created_time, modified_time, index_code, index_name, data_source)' \
      'values (now(), now(), "{code}", "{name}", "蛋卷基金");'
with open('index.txt', 'r') as f:
    for line in f.readlines():
        ds = line.replace('\n', '').split(',')
        print(sql.format(code=ds[0], name=ds[1]))
