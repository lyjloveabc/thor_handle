"""
临时
"""
from utils.constant.constant import Constant


class Temp:
    def __init__(self):
        pass

    def handle(self):
        pass


if __name__ == '__main__':

    with open(Constant.BASE_PATH + 'mobile.txt', 'r') as f:
        for line in f.readlines():
            sql = 'update admin_employee set job_post_id = jpid where mobile = "{mobile}";'
            print(sql.format(mobile=line[:-1]))

    temp = Temp()
    temp.handle()
