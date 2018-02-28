sql = 'UPDATE itl_parking SET house_info_id = "{hId}", contact = "{contact}", contact_mobile = "{contact_mobile}" WHERE name = "{name}";'
sql_2 = 'UPDATE itl_parking SET house_info_id = null, contact = "{contact}", contact_mobile = "{contact_mobile}" WHERE name = "{name}";'
house_db = dict()

with open('file/zd_house.txt', 'r') as f:
    for row in f.readlines():
        data = row.split(',')
        house_db[str(int(data[1])) + '-' + str(int(data[2])) + '-' + str(int(data[3]))] = data[0]

with open('file/车位所有者.txt', 'r') as f:
    for row in f.readlines():
        if row == '':
            continue
        data = row.replace('\n', '').split('\t')

        try:
            if data[1] in house_db:
                print(sql.format(hId=house_db[data[1]], contact=data[2], contact_mobile=data[3], name=data[0]))
            else:
                print(sql_2.format(contact=data[2], contact_mobile=data[3], name=data[0]))
        except:
            print('----', data)
