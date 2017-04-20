"""
验证田阳登录
"""
import requests
import json


class SkyLogin:
    __BASE_PATH = 'file/'

    def __init__(self):
        self.base_url = 'http://api3.itianluo.cn/login_new_ty?mobile={account}&login_type=101&pwd={pwd}'

    def handle(self):
        account_pwd_group = self.get_account_pwd_group()

        for account_pwd in account_pwd_group:
            is_ok_flag = self.is_ok(account_pwd)
            print(account_pwd, is_ok_flag)

    @staticmethod
    def get_account_pwd_group():
        account_pwd_group = list()

        account_pwd = {
            'account': '18768111223',
            'pwd': '123456'
        }
        account_pwd_group.append(account_pwd)
        return account_pwd_group

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
