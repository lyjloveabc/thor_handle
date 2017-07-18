"""
处理菜单
"""
import csv
import re

from utils.file.excel.readUtil import ReadUtil


class ToLegal:
    _TYPE = {'确认': '1A', '拍照': '1B', '检查': '1C', '抽检': '1D', '巡更': '1E'}
    _RATE = {'日': 'D', '周': 'W', '月': 'M', '年': 'Y'}
    _ROLE_ALL = {
        '第一权限管理员': '第一权限管理员', '项目负责人': '项目负责人', '客服负责人': '客服负责人', '保洁负责人': '保洁负责人',
        '保洁': '保洁', '绿化负责人': '绿化负责人', '绿化': '绿化', '保安负责人': '保安负责人', '门岗': '门岗',
        '巡逻岗': '巡逻岗', '监控岗': '监控岗', '车库岗': '车库岗', '工程负责人': '工程负责人', '工程': '工程', '外部维修商': '外部维修商',
        '财务': '财务', '外围观测者': '外围观测者', '苹果审核专用': '苹果审核专用', '巡更': '巡更', '业委会': '业委会',
        '管家客服': '管家客服', '前台客服': '前台客服', '保安领班': '保安领班', '高配': '高配', '弱电': '弱电',
        '行政内务': '行政内务', '抽检': '抽检', '小二': '小二', '物业公司管理员': '物业公司管理员', '后台项目管理员': '后台项目管理员'
    }

    def __init__(self, *args, **kw):
        print('init object')

    def handle(self, file_name):
        field_index = {'role': 0, 'type': 1, 'content': 2, 'standard': 3, 'rate': 4, 'startTime': 5, 'endTime': 6}

        self.write_file(ReadUtil.read_file(file_name, field_index), file_name)

    @staticmethod
    def write_file(data, file_name):
        with open('out_' + re.search(r'(.+)\.', file_name).group(1) + '.csv', 'w', encoding='gbk') as csv_file:
            csv_writer = csv.writer(csv_file, dialect='excel')

            for row in data:
                if ToLegal._check_param(row):
                    csv_writer.writerow([ToLegal._type_name_to_type(row['type']), ToLegal._transform_text(row['content']),
                                         ToLegal._transform_text(row['standard']), ToLegal._rate_name_to_rate(row['rate']),
                                         int(row['startTime']), int(row['endTime']), ToLegal._ROLE_ALL[row['role']], row['role']])
                else:
                    print(row)

    @staticmethod
    def _check_param(row):
        try:
            start_time = int(row['startTime'])
            end_time = int(row['endTime']) if int(row['endTime']) != -1 else 1

            flag = row['type'] != '' \
                   and row['type'] in ToLegal._TYPE.keys() \
                   and len(row['content'].strip()) <= 256 \
                   and len(row['content'].strip()) <= 512 \
                   and row['rate'] in ToLegal._RATE.keys() \
                   and start_time <= end_time \
                   and row['role'] in ToLegal._ROLE_ALL.keys()
            return flag
        except Exception as e:
            print(e)
            return False
        finally:
            pass

    @staticmethod
    def _type_name_to_type(type_name):
        return ToLegal._TYPE[type_name] if type_name in ToLegal._TYPE else ''

    @staticmethod
    def _rate_name_to_rate(rate_name):
        return ToLegal._RATE[rate_name] if rate_name in ToLegal._RATE else ''

    @staticmethod
    def _transform_text(text):
        return str(text).strip().replace(',', '，').replace('\n', '')


if __name__ == '__main__':
    handle = ToLegal()
    handle.handle('房总任务库-20170718删除泳池版 .xlsx')
