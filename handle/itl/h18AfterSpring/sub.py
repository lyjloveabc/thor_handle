"""
自动化一次性全部处理完成
"""
import os

from handle.global_setting import DEFAULT_DB_ENV
from handle.itl.h18AfterSpring.hqUser import HqUser
from utils.constant.constant import Constant


class Sub:
    def __init__(self):
        # 必须保持跟线上同步的数据库表
        self.now_update = [
            'user',
            'user_role_relation',
            'zones',
            'itl_company',
            'itl_user_zone_relation',
            'itl_zone_category',
        ]


if __name__ == '__main__':
    dao = DEFAULT_DB_ENV  # 数据库连接对象
    file = 'file/out_sub.sql'  # 输出的sql文件

    if os.path.exists(file):
        os.remove(file)  # 删除已经存在的输出文件

    # 写入事物的开始sql语句
    with open(file, 'a') as f:
        f.write(Constant.SQL_BEGIN)
        f.write('\n')

    # 公明物业的总部人员小区处理
    hqUser = HqUser(dao)
    hqUser.h(file)

    # 写入事物的结束sql语句
    with open(file, 'a') as f:
        f.write(Constant.SQL_COMMIT)
        f.write('\n')
