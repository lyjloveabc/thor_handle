"""
校验天眼登录
select account, password from user;
"""
import requests
import json

from utils.constant.constant import Constant


class SkyLogin:
    __BASE_PATH = 'file/'

    def __init__(self):
        self.base_url = 'http://api3.itianluo.cn/login_new_ty?mobile={account}&login_type=101&pwd={pwd}'

    def handle(self):
        account_pwd_group = self.get_account_pwd_group(Constant.BASE_PATH + 'user_20170506.txt')

        for account_pwd in account_pwd_group:
            is_ok_flag = self.is_ok(account_pwd)
            print(account_pwd, is_ok_flag)

    @staticmethod
    def get_account_pwd_group(file):
        data = list()
        with open(file, 'r') as f:
            for line in f.readlines():
                line_split = line[:-1].split(',')
                item = {
                    'account': line_split[0],
                    'pwd': line_split[0],
                }
                data.append(item)
        return data

    def is_ok(self, account_pwd):
        is_ok_flag = False

        response = requests.get(self.base_url.format(account=account_pwd['account'], pwd=account_pwd['pwd']))
        status_code = response.status_code
        if status_code == 200:
            text = json.loads(response.text)
            if text['login_result'] == 1:
                is_ok_flag = True

        return is_ok_flag


if __name__ == '__main__':
    SkyLogin().handle()
