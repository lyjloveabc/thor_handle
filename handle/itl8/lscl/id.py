_51 = list()
with open('51.txt', 'r') as f:
    for row in f.readlines():
        _51.append(row.replace('\n', ''))

_53 = list()
with open('53.txt', 'r') as f:
    for row in f.readlines():
        _53.append(row.replace('\n', ''))

for row in _53:
    if row not in _51:
        print(row)

print("----")
for row in _51:
    if row not in _53:
        print(row)
