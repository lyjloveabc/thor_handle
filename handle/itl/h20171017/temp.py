online = list()
asu = list()

with open('file/线上出账的车位号.txt', 'r') as f:
    for line in f.readlines():
        online.append(line[:-1])

with open('file/pa.txt', 'r') as f:
    for line in f.readlines():
        asu.append(line[:-1])

for asu_un in asu:
    if asu_un not in online:
        print(asu_un)
