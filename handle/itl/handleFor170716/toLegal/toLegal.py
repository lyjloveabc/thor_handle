"""
处理菜单
"""
from openpyxl import Workbook

from handle.itl.handleFor170716.dbUtil import DbUtil
from utils.file.excel.readUtil import ReadUtil


class ToLegal:
    _TYPE = {'确认': '1A', '拍照': '1B', '检查': '1C', '抽检': '1D', '巡更': '1E'}
    _RATE = {'日': 'D', '周': 'W', '月': 'M', '年': 'Y'}
    _ROLE = []

    def __init__(self, *args, **kw):
        self.dbUtil = kw['dbUtil']
        _ROLE = self.dbUtil.get_all_role()

    def handle(self):
        field_index = {
            'role': 0,
            'type': 1,
            'content': 2,
            'standard': 3,
            'rate': 4,
            'startTime': 5,
            'endTime': 6,
        }

        self.write_file(ReadUtil.read_file('职能类型版任务库-测试.xlsx', field_index))

    @staticmethod
    def write_file(data):
        a = list()
        wb = Workbook()  # 在内存中创建一个workbook对象，而且会至少创建一个 worksheet
        ws = wb.active  # 获取当前活跃的worksheet,默认就是第一个worksheet

        for index in range(1, len(data)):
            if ToLegal._check_param(data[index]):
                print(data[index])
                a.append(data[index])
            else:
                ws.cell(row=index, column=1).value = ToLegal._type_name_to_type(data[index]['type'])
                ws.cell(row=index, column=2).value = data[index]['content'].strip()
                ws.cell(row=index, column=3).value = data[index]['standard'].strip()
                ws.cell(row=index, column=4).value = ToLegal._rate_name_to_rate(data[index]['rate'])
                ws.cell(row=index, column=5).value = int(data[index]['startTime'])
                ws.cell(row=index, column=6).value = int(data[index]['endTime'])
                ws.cell(row=index, column=7).value = data[index]['role']
                ws.cell(row=index, column=8).value = data[index]['role']

        wb.save(filename="/Users/luoyanjie/abc2223.xlsx")  # 保存

    @staticmethod
    def _check_param(row):
        start_time = int(row['startTime'])
        end_time = int(row['endTime']) if int(row['endTime']) != -1 else 1
        print(row['type'] in ToLegal._TYPE)
        print()
        return row['type'] in ToLegal._TYPE \
               and len(row['content'].strip()) <= 256 \
               and len(row['content'].strip()) <= 512 \
               and row['rate'] in ToLegal._RATE \
               and start_time <= end_time \
               and row['role'] in ToLegal._ROLE

    @staticmethod
    def _type_name_to_type(type_name):
        return ToLegal._TYPE[type_name] if type_name in ToLegal._TYPE else ''

    @staticmethod
    def _rate_name_to_rate(rate_name):
        return ToLegal._RATE[rate_name] if rate_name in ToLegal._RATE else ''


if __name__ == '__main__':
    handle = ToLegal(**{'dbUtil': DbUtil()})
    handle.handle()
