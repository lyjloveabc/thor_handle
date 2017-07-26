import csv
import re
from datetime import datetime

from utils.file.excel.readUtil import ReadUtil

__author__ = 'Thor'


class TaskExcelToLegalCsv:
    """ 运营整理的任务excel文件转换成合法的可以直接导入的csv文件。Created by Thor on 2017/07/07. """

    # 任务类型
    _TYPE = {'确认': '1A', '拍照': '1B', '检查': '1C', '抽检': '1D', '巡更': '1E'}

    # 任务频率
    _RATE = {'日': 'D', '周': 'W', '月': 'M', '年': 'Y'}

    # 这里的职能没使用数据库实时数据，所以后续如果职能有调整或更新的话，这里也需要调整更新
    _ROLE_ALL = {
        '第一权限管理员': '第一权限管理员', '项目负责人': '项目负责人', '客服负责人': '客服负责人', '保洁负责人': '保洁负责人',
        '保洁': '保洁', '绿化负责人': '绿化负责人', '绿化': '绿化', '保安负责人': '保安负责人', '门岗': '门岗',
        '巡逻岗': '巡逻岗', '监控岗': '监控岗', '车库岗': '车库岗', '工程负责人': '工程负责人', '工程': '工程', '外部维修商': '外部维修商',
        '财务': '财务', '外围观测者': '外围观测者', '苹果审核专用': '苹果审核专用', '巡更': '巡更', '业委会': '业委会',
        '管家客服': '管家客服', '前台客服': '前台客服', '保安领班': '保安领班', '高配': '高配', '弱电': '弱电',
        '行政内务': '行政内务', '抽检': '抽检', '小二': '小二', '物业公司管理员': '物业公司管理员', '后台项目管理员': '后台项目管理员'
    }

    # csv编码格式
    _CSV_ENCODING = 'gbk'

    def __init__(self, *args, **kw):
        print("init object!")

    def handle(self, file_name):
        field_index = {'role': 0, 'type': 1, 'content': 2, 'standard': 3, 'rate': 4, 'startTime': 5, 'endTime': 6}

        self.write_file(ReadUtil.read_file(file_name, field_index), file_name)

    @staticmethod
    def write_file(data, file_name):
        """ 写如csv文件，如果原始excel中，某一行数据有问题，则不写入到最终csv文件中，会在控制台显示出有问题的行 """
        target = 'out_' + re.search(r'(.+)\.', file_name).group(1) + datetime.now().strftime('%Y%m%d%H%M%S') + '.csv'  # 最终的文件全路径（包括路径和文件名）

        with open(target, 'w', encoding=TaskExcelToLegalCsv._CSV_ENCODING) as csv_file:
            csv_writer = csv.writer(csv_file, dialect='excel')  # 文件方言为excel

            for row in data:
                if TaskExcelToLegalCsv._check_param(row):
                    # 数据按行写入到csv
                    csv_writer.writerow([TaskExcelToLegalCsv._type_name_to_type(row['type']), TaskExcelToLegalCsv._transform_text(row['content']),
                                         TaskExcelToLegalCsv._transform_text(row['standard']), TaskExcelToLegalCsv._rate_name_to_rate(row['rate']),
                                         int(row['startTime']), int(row['endTime']), TaskExcelToLegalCsv._ROLE_ALL[row['role']], row['role']])
                else:
                    print(row)  # 有问题的行打印到控制

    @staticmethod
    def _check_param(row):
        """ 检查每一行记录的数据是否合法，合法直接返回True，数据有问题则直接返回False """
        try:
            start_time = int(row['startTime'])
            end_time = int(row['endTime']) if int(row['endTime']) != -1 else 1  # 完成时间为-1表示的是日任务可以延期，这里做一下特殊处理，方便后续计算

            return row['type'] != '' \
                   and row['type'] in TaskExcelToLegalCsv._TYPE.keys() \
                   and len(row['content'].strip()) <= 256 \
                   and len(row['content'].strip()) <= 512 \
                   and row['rate'] in TaskExcelToLegalCsv._RATE.keys() \
                   and start_time <= end_time \
                   and row['role'] in TaskExcelToLegalCsv._ROLE_ALL.keys()
        except Exception as e:
            print(e)
            return False
        finally:
            pass

    @staticmethod
    def _type_name_to_type(type_name):
        """ 根据任务类型中文名称，获取任务类型编码 """
        return TaskExcelToLegalCsv._TYPE[type_name] if type_name in TaskExcelToLegalCsv._TYPE else ''

    @staticmethod
    def _rate_name_to_rate(rate_name):
        """ 根据任务频率中文名称，获取任务频率编码 """
        return TaskExcelToLegalCsv._RATE[rate_name] if rate_name in TaskExcelToLegalCsv._RATE else ''

    @staticmethod
    def _transform_text(text):
        """ 原始数据处理：去掉文本的首尾空字符串，把英文逗号转换为中文逗号，把所有的换行符都去掉 """
        return str(text).strip().replace(',', '，').replace('\n', '')


if __name__ == '__main__':
    base_path = ''
    handle = TaskExcelToLegalCsv()

    handle.handle(base_path + '20170725景江苑任务库迁移梳理-韦护.xls')
    handle.handle(base_path + '20170725碧景园任务库迁移梳理-韦护.xls')
    handle.handle(base_path + '20170725黄龙雅苑任务库迁移梳理-韦护.xls')
    handle.handle(base_path + '万源城依据.xlsx')
    handle.handle(base_path + '东园高层.xlsx')
    handle.handle(base_path + '中山御庭.xlsx')
    handle.handle(base_path + '凯喜雅大厦.xlsx')
    handle.handle(base_path + '北海公园.xlsx')
    handle.handle(base_path + '政苑小区.xlsx')
    handle.handle(base_path + '时代长岛之春.xlsx')
    handle.handle(base_path + '臻园.xlsx')
    handle.handle(base_path + '西溪金座.xlsx')
