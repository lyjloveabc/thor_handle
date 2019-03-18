h_m = dict()

with open('house_2.txt', 'r') as f:
    for row in f.readlines():
        d_a = row.replace('\n', '').split(',')
        h_m[d_a[1]] = d_a[0]

with open('lyj.txt', 'r') as f:
    for row in f.readlines():
        row = row.replace('\n', '')
        d_a = row.split('\t')
        if h_m[d_a[0]]:
            print(len(d_a[0]))
