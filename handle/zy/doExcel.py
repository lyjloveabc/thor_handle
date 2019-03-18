import os

sql = 'INSERT INTO itl_car_info(gmt_create, gmt_modified, name, house_info_id) VALUES (now(), now(), \'{name}\', \'{h_id}\');'

h_m = dict()  # 原始的房号数据
need = list()  # 读进来的数据
ok_data = list()  # 处理后OK的数据
error_data = list()  # 处理后错误的数据

if os.path.exists('out/ok.txt'):
    os.remove('out/ok.txt')  # 删除文件
if os.path.exists('out/error.txt'):
    os.remove('out/error.txt')  # 删除文件

with open('house_2.txt', 'r') as f:
    for row in f.readlines():
        d_a = row.replace('\n', '').split(',')
        h_m[str(d_a[1])] = d_a[0]

with open('lyj.txt', 'r') as f:
    for row in f.readlines():
        row = row.replace('\n', '')
        d_a = row.split('\t')
        need.append(d_a)

for row in need:
    if str(row[0]) in h_m.keys() and len(row) > 1 and row[1] is not None and row[1] != '':
        h_id = h_m[row[0]]
        car_no_array = str(row[1]).split(',')
        for c in car_no_array:
            ok_data.append(
                sql.format(name=c, h_id=h_id)
            )
    else:
        if str(row[0]) not in h_m.keys():
            error_data.append('数据库没有该房号: ' + str(row) + '\n')
        if not (len(row) > 1 and row[1] is not None and row[1] != ''):
            error_data.append('车牌字段没有: ' + str(row) + '\n')

with open('out/ok.txt', 'a') as ok_f:
    for row in ok_data:
        ok_f.write(str(row) + '\n')

with open('out/error.txt', 'a') as error_f:
    for row in error_data:
        error_f.write(str(row))
