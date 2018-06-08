import datetime
import json
import requests


class PostThing:
    def __init__(self):
        self.today = datetime.datetime.now()
        self.file_date_str = '_' + self.today.strftime('%Y%m%d')

        self.ENV_IP = '127.0.0.1:8001'
        # self.ENV_IP = 'prenewcloud.itianluo.cn'
        self.url = 'http://{ENV_IP}/postThing/launchForHold.do?app=AJ&client=iPhone&version=1.6.4&outerType=users&token=9d70a03b613349633bb397a0a2e9c57d&userId=4147&zoneId=1&houseInfoId=3139' \
            .format(ENV_IP=self.ENV_IP)

    def handle(self):
        param = {
            # 'app': 'GJ',
            # 'client': 'iPhone',
            # 'version': '1.6.6',
            # 'outerType': 'STAFF',
            # 'token': '77f56c02a13b828aa80769cf495cf0fc',
            # 'userId': '35',

            'contentType': 'SAFETY',
            'content': '1',
            # 'images': '',
        }

        # headers = {'content-type': 'application/json'}
        headers = {}
        response = requests.post(self.url, headers=headers, data=param)
        json_data = json.loads(response.text)
        print(json_data)


if __name__ == '__main__':
    tjMd = PostThing()
    tjMd.handle()
