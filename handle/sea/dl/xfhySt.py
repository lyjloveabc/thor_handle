# 处理日期
day = '210801'

# 读取动量榜前排的数据
part = dict()
with open('data{}/part.txt'.format(day), 'r', encoding="UTF-8-sig") as f:
    for row in f.readlines():
        row = row.replace('\n', '')

        if row in part:
            part[row] = part[row] + 1
        else:
            part[row] = 1
print('part: ', part)

# 读取所有数据
total = dict()
with open('data{}/total.txt'.format(day), 'r', encoding="UTF-8-sig") as f:
    for row in f.readlines():
        row = row.replace('\n', '')

        if row in total:
            total[row] = total[row] + 1
        else:
            total[row] = 1
print('total: ', total)

# 计算板块的动量分值
res = dict()
for k, v in total.items():
    score = 0
    if k in part:
        score = part[k] * part[k] / total[k]
    else:
        score = 0
    res[k] = score
print('res: ', res)

# 输出结果
with open('data{}/res.txt'.format(day), 'w', encoding="UTF-8-sig") as f:
    f.truncate()
    for row in sorted(res.items(), key=lambda kv: (kv[1], kv[0]), reverse=True):
        f.write(row[0] + ':  ' + str(round(float(row[1]), 3)) + '\n')
