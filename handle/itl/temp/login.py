"""
爱家端登录
"""
import datetime
import json

import requests


class UserData:
    def __init__(self):
        self.today = datetime.datetime.now()
        self.today_int = int(self.today.strftime('%Y%m%d'))
        self.file_date_str = '_' + str(self.today_int)

        self.base_url = 'http://preapi.itianluo.cn/login_block'
        self.param = {
            "device": "ios",
            "installationId": "096064D4-A5DD-4996-A2D5-E97E82F42F21",
            "mobile": "15669016778",
            "p1": "7686",
            "p2": "1010101",
            "p3": "2",
            "p_code": "1",
            "p_type": "2",
            "p_version": "1.4.4",
            "pwd": "123456",
            "version": "1.4.4"
        }

    def h(self):
        response = requests.post(self.base_url, data=self.param)
        result_data = json.loads(response.text)

        print(response.text)


if __name__ == '__main__':
    ud = UserData()
    ud.h()
