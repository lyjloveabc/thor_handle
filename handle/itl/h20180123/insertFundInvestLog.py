import json

import requests


class InsertFundInvestLog:
    def __init__(self):
        self.ENV = 'http://127.0.0.1:7001'

    def handle(self):
        with open('fundInvestLog.json', 'r') as f:
            data = json.load(f)
        for row in data:
            response = requests.post(self.ENV + '/fundInvestLog/fundInvestLog', data=row)
            print(response.text)


if __name__ == '__main__':
    ifil = InsertFundInvestLog()
    ifil.handle()
