a = list()
with open('important/id.txt', 'r') as f:
    for row in f.readlines():
        data = row.replace('\n', '').split('\t')
        a.append({'id': data[0], 'category': data[3]})

print(a)