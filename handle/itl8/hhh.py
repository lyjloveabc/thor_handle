# with open('hahapp.txt', 'r') as f:
#     idx = 1
#     for line in f.readlines():
#         row = line.replace('\n', '').split(',')
#         print('(' + str(idx) + ', now(), now(), ' + str(row[0]) + ', ' + str(row[1]) + '),')
#         idx += 1

idx = 42
for row in range(42, 57):
    print('({id}, now(), now(), {hah}),'.format(id=idx, hah=idx))

    idx += 1
