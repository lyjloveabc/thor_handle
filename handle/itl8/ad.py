with open('adsasdasd.txt', 'r') as f:
    idx = 3777
    for line in f.readlines():
        row = line.replace('\n', '')
        print('(' + str(idx) + ', now(), now(), \' ' + line.replace('\n', '') + '\', \'HOUSEKEEPER_MY_TAB_我的绩效\'),')
        idx += 1
