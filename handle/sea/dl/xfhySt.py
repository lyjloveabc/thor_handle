part = dict()
with open('part.txt', 'r', encoding="UTF-8-sig") as f:
    for row in f.readlines():
        row = row.replace('\n', '')

        if row in part:
            part[row] = part[row] + 1
        else:
            part[row] = 1
print(part)

all = dict()
with open('all.txt', 'r', encoding="UTF-8-sig") as f:
    for row in f.readlines():
        row = row.replace('\n', '')

        if row in all:
            all[row] = all[row] + 1
        else:
            all[row] = 1
print(all)

res = dict()
for k, v in all.items():
    print(part[k], all[k])
    score = 0
    if k in part:
        score = part[k] * part[k] / all[k]
    else:
        score = 0
    res[k] = score

print(res)

for row in sorted(res.items(), key=lambda kv: (kv[1], kv[0]), reverse=True):
    print(row[0], row[1])
