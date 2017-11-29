import json
import requests


class AutoClearLog:
    def __init__(self):
        pass

    def handle(self):
        headers = {'content-type': 'application/json'}
        json = {
            "accessory": [

            ],
            "app": "GJ",
            "approvalFlow": [
                {
                    "exeUserId": [
                        415
                    ],
                    "categoryId": -2
                }
            ],
            "expenseItemDetail": [
                {
                    "expenseItemId": 1,
                    "money": 10,
                    "remark": "通过python测试222222"
                }
            ],
            "images": [

            ],
            "type": "STANDARD",
            "useTime": 201711,
            "userId": 35,
            "zoneId": 1
        }
        response = requests.post(
            "http://prenewcloud.itianluo.cn/budget/approval.do?app=GJ&client=iPhone&outerType=STAFF&token=77f56c02a13b828aa80769cf495cf0fc&userId=35&version=1.6.1&zoneId=1",
            headers=headers, json=json)
        # response = requests.post("http://127.0.0.1:8001/budget/approval.do?app=1", headers=headers, data=data)
        print(response)


if __name__ == '__main__':
    acl = AutoClearLog()
    acl.handle()
