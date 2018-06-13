import datetime
import json
import requests


class Dododo:
    def __init__(self):
        self.today = datetime.datetime.now()
        self.file_date_str = '_' + self.today.strftime('%Y%m%d')

        # self.ENV_IP = '127.0.0.1:8001'
        self.ENV_IP = 'prenewcloud.itianluo.cn'
        self.url = 'http://{ENV_IP}/usedInLua/batchCreateEnergyBill?periodId=381&operatorId=431' \
            .format(ENV_IP=self.ENV_IP)

    def handle(self):
        param = {

        }

        # headers = {'content-type': 'application/json'}
        headers = {}
        response = requests.post(self.url, headers=headers, data=param)
        json_data = json.loads(response.text)
        print(json_data)


if __name__ == '__main__':
    tjMd = Dododo()
    tjMd.handle()
