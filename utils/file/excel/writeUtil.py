"""
写excel
"""
import logging

import openpyxl
from openpyxl import Workbook

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger(__name__)


class WriteUtil:
    @staticmethod
    def write07Excel(path):
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.title = 'ios埋点统计数据'

        value = [["名称", "价格", "出版社", "语言"],
                 ["如何高效读懂一本书", "22.3", "机械工业出版社", "中文"],
                 ["暗时间", "32.4", "人民邮电出版社", "中文"],
                 ["拆掉思维里的墙", "26.7", "机械工业出版社", "中文"]]
        for i in range(0, 4):
            for j in range(0, len(value[i])):
                sheet.cell(row=i + 1, column=j + 1, value=str(value[i][j]))

        wb.save(path)
        print("写入数据成功！")
