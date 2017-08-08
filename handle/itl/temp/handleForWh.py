base_sql = 'INSERT INTO itl_job_title VALUES ("{id}", now(), now(), "{name}", "", "{remark}", "公司总部");'

with open('hehe.txt', 'r') as f:
    index = 19
    for line in f.readlines():
        hehe = line[:-1].split('	')
        print(base_sql.format(id=index, name=hehe[0], remark=hehe[1]))
        index += 1
