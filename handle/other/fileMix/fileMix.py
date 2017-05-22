"""
二进制读取文件
添加删除其中字节
"""
import os
import logging

from utils.constant.constant import Constant
from utils.constant.resultCode import ResultCode
from utils.system.systemUtil import SystemUtil


class FileMix:
    def __init__(self):
        pass

    @staticmethod
    def handle(path=os.getcwd(), extension=None, go_deep=True):
        # 获取指定目录下的所有文件和目录名
        file_name_group = os.listdir(path)

        for file_name in file_name_group:
            # 连接目录与文件名或目录
            old_full_file_name = os.path.join(path, file_name)

            if extension is None or Constant.DOT not in old_full_file_name or old_full_file_name.split(Constant.DOT)[1] in extension:
                is_file = os.path.isfile(old_full_file_name)
                is_dir = os.path.isdir(old_full_file_name)

                if is_file:
                    with open(old_full_file_name, 'wb') as f:
                        f.write(bytes('hahCP', encoding="utf8"))
                elif is_dir and go_deep:
                    FileMix.handle(path=old_full_file_name)
                else:
                    logging.error(ResultCode.CONDITION_NOT_CONFORM)
        pass


if __name__ == '__main__':
    data = '/Users/luoyanjie/temp'

    obj = FileMix()
    obj.handle(data)
    SystemUtil.batch_rename_file_2(data)
