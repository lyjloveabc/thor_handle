from utils.file.excel.excelReadUtil import ExcelReadUtil
# ExcelReadUtilfrom utils.file.excel.readUtil import ReadUtil
#
# field_index = {
#     'B_DATE': 0,
#     'S_DATE': 1,
#     'NAME': 2,
#     'B_PRICE': 3,
#     'B_TOTAL': 4,
#     'S_PRICE': 5,
#     'S_TOTAL': 6,
#     'NUM': 7,
#     'PROFIT': 8,
#     'RATE(%)': 9
# }
#
# file_name = 'operate_log_all.xlsx'
# data = ReadUtil.read_file(file_name, field_index)

field_index_dict = {
            'house_code': 0,
            'last_num': 1,
            'current_num': 2,
        }
source_sub_enter = ExcelReadUtil.read_f7ile('operate_log_all.xlsx', field_index_dict)
