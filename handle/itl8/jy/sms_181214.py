import requests

url = 'http://127.0.0.1:8001/external/moreBatchSendSmsForCommon'
# sms_mobile = [
#     "13095960110",
#     "13857897503",
#     "13806672021",
#     "13306631393",
#
#     "13706846056",
#     "13056900008",
#     "18957886499",
#     "13867862678",
#     "13967838700",
#     "13805878758",
#     "13906687349",
#     "13967836952",
#     "13777941043",
#
#     "13738857018",
#     "15825552875"
# ]

sms_mobile = [
    '13805878758'
]

r = requests.post(url, data={'temp': 'StoreBillAsk', 'mobileList': sms_mobile})
