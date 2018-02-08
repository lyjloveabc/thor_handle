import json

import requests


class InsertFundInvestLog:
    def __init__(self):
        # self.ENV = 'http://127.0.0.1:7001'
        self.ENV = 'http://127.0.0.1:7001'
        self.ENV_PROD = 'http://121.43.166.200:7001'

    def handle(self):
        with open('fundInvestLog_20180208.json', 'r') as f:
            data = json.load(f)
        for row in data:
            response = requests.post(self.ENV_PROD + '/fundInvestLog/fundInvestLog', data=row)
            print(response.text)


if __name__ == '__main__':
    ifil = InsertFundInvestLog()
    ifil.handle()
