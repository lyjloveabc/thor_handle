import re

import requests

from utils.file.excel.readUtil import ReadUtil


def len_sort(elem):
    return len(elem) == 11


url = 'http://newcloud.itianluo.cn/external/moreBatchSendSmsForCommon'
data = ReadUtil.read_file('发短信电话-20181213.xls', {'z': 0, 'm': 1, 's': 2, 'name': 3, 'mobile': 4})  # 原始数据
xxx = list()
with open('error.txt', 'r') as f:
    for row in f.readlines():
        line = row.replace('\n', '')
        hhh = re.search('.+:(\d+).0备注：', line)
        if hhh is not None:
            xxx.append(
                re.search('.+:(\d+).0备注：', line).group(1)
            )
need_send_mobile = list()  # 需要发送的手机号
need_send = list()  # 可以发送
error = list()  # 无法发送的错误的手机号

for row in data:
    if len(row['mobile']) == 11:
        need_send_mobile.append(row['mobile'])
        need_send.append(row)
    else:
        if len(row['mobile']) < 11:
            error.append(row)
        else:
            ms_array = str(row['mobile']).replace(' /', '/').replace('  ', '/').replace('、', '/').replace(' ', '/').split('/')
            ms_array.sort(key=len_sort, reverse=True)
            flag_info = ''
            for ms in ms_array:
                if len(ms) == 11:
                    need_send_mobile.append(ms)
                    need_send.append(row)
                    flag_info += ms
                else:
                    if flag_info is not None and flag_info != '':
                        row['info'] = '该房已用{mobile}发送'.format(mobile=flag_info)
                    error.append(row)

# need_send_mobile = ['18768111223']
for x in xxx:
    print(x)

# xxx = ['18768111223']

r = requests.post(url, data={'temp': 'anniversaryGiftGiving', 'mobileList': xxx})

# print("-----------已发送：")
# for row in need_send:
#     print(row['z'] + ' ' + row['m'] + ' ' + row['s'] + ' ' + '业主姓名为<' + row['name'] + '>，发送号码：' + str(row['mobile']).replace('/', '、'))
# print("")
# print("-----------数据有误无法发送：")
# for row in error:
#     if 'info' in row.keys():
#         print(row['z'] + ' ' + row['m'] + ' ' + row['s'] + ' ' + '业主姓名为<' + row['name'] + '>，错误手机号: ' + row['mobile'] + ' 备注：' + row['info'])
#     else:
#         print(row['z'] + ' ' + row['m'] + ' ' + row['s'] + ' ' + '业主姓名为<' + row['name'] + '>，错误手机号:  ' + row['mobile'] + ' 备注：')
