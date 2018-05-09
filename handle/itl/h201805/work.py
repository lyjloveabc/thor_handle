import datetime
import json
import requests


class Work:
    def __init__(self):
        self.today = datetime.datetime.now()
        self.file_date_str = '_' + self.today.strftime('%Y%m%d')

        self.ENV_IP = '127.0.0.1:8001'
        self.url = 'http://{ENV_IP}/work/workList.do?app=GJ&client=iPhone&version=1.6.6&outerType=STAFF&token=77f56c02a13b828aa80769cf495cf0fc&userId=35' \
            .format(ENV_IP=self.ENV_IP)

    def handle(self):
        fz = {
            'taskListFrom': 'TASK_CENTER'
        }

        param = {
            'app': 'GJ',
            'client': 'iPhone',
            'version': '1.6.6',
            'outerType': 'STAFF',
            'token': '77f56c02a13b828aa80769cf495cf0fc',
            'userId': '35',

            'zoneId': '1',
            'pageNum': '1',
            'pageSize': '20',
            'workType': 'TASK',
            'workListSearch': json.dumps(fz)
        }

        print(json.dumps(param))
        print(self.url)
        headers = {'content-type': 'application/json'}
        response = requests.post(self.url, headers=headers, data=json.dumps(param))
        json_data = json.loads(response.text)
        print(json_data)


if __name__ == '__main__':
    tjMd = Work()
    tjMd.handle()
