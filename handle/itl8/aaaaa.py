a = list()
with open('/Users/luoyanjie/修改已付和欠费的账单ID.txt', 'r') as f:
    for row in f.readlines():
        row = row.replace('\n', '')
        a.append(row)
print(','.join(a))