import datetime
import json
import requests


class UnitTest:
    def __init__(self):
        self.today = datetime.datetime.now()
        self.file_date_str = '_' + self.today.strftime('%Y%m%d')

        # self.ENV_IP = '127.0.0.1:8001'
        self.ENV_IP = 'prenewcloud.itianluo.cn'
        self.url = 'http://{ENV_IP}/label/addBizLabel.do'.format(ENV_IP=self.ENV_IP)
        self.url += '?app=GJ&client=iPhone&version=1.6.6&outerType=STAFF&token=77f56c02a13b828aa80769cf495cf0fc&userId=35&zoneId=1'

    def handle(self):
        param = {
            'bizType': 'POST_THING',
            'bizId': '190',
            'operateType': '无需处理',
            'labels': ['呵呵', '哈哈哈'],
        }

        # self.url += '&bizType=POST_THING&bizId=190&operateType=无需处理'

        headers = {'content-type': 'application/json'}
        # headers = {}
        response = requests.post(self.url, headers=headers, data=json.dumps(param))
        # response = requests.get(self.url, headers=headers)
        json_data = json.loads(response.text)
        print(json_data)


if __name__ == '__main__':
    ut = UnitTest()
    ut.handle()
