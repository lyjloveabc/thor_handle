import datetime
import json
import requests


class Shua:
    def __init__(self):
        self.today = datetime.datetime.now()
        self.file_date_str = '_' + self.today.strftime('%Y%m%d')

        self.url = 'https://wenku.baidu.com/view/726af47a27284b73f242504f'

    def handle(self):
        response = requests.get(self.url)
        print(response)

if __name__ == '__main__':
    tjMd = Shua()
    tjMd.handle()
