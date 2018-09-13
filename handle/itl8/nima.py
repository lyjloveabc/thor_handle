h = list()
with open('车位id.txt', 'r') as f:
    for row in f.readlines():
        x = row.replace('\n', '')
        h.append(x)

print(",".join(h))
