"""
自动化一次性全部处理完成
"""
import os

from handle.global_setting import DEFAULT_DB_ENV
from handle.itl.h18AfterSpring.batchCreateHqZone import BatchCreateHqZone
from utils.constant.constant import Constant


class Main_1:
    def __init__(self):
        # 必须保持跟线上同步的数据库表
        self.now_update = {
            'itl_company',
            'zones',
        }


if __name__ == '__main__':
    dao = DEFAULT_DB_ENV  # 数据库连接对象
    file = 'file/out_1.sql'  # 输出的sql文件

    if os.path.exists(file):
        os.remove(file)  # 删除已经存在的输出文件

    # 写入事物的开始sql语句
    with open(file, 'a') as f:
        f.write(Constant.SQL_BEGIN)
        f.write('\n')

    # 处理总部小区：根据现有公司生成总部小区、总部人员处理
    batchCreateHqZone = BatchCreateHqZone(dao)
    batchCreateHqZone.h(file)

    # 写入事物的结束sql语句
    with open(file, 'a') as f:
        f.write(Constant.SQL_COMMIT)
        f.write('\n')