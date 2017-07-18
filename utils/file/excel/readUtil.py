import logging
import xlrd

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger(__name__)

__author__ = 'Thor'


class ReadUtil:
    """ 读取excel工具类 """

    @staticmethod
    def read_file(file_name, field_index, include_first=False):
        """ 读取excel默认的方法 """
        result_list = list()
        data = xlrd.open_workbook(file_name)

        for sheet in data.sheets():
            rows = sheet.nrows
            if include_first:
                ran = range(rows)
            else:
                ran = range(1, rows)

            for i in ran:
                try:
                    row_data = dict()
                    for k, v in field_index.items():
                        row_data[k] = sheet.row_values(i)[v]

                    result_list.append(row_data)
                except ValueError as e:
                    log.error(e)
        log.info(file_name + ' :: ' + str(len(result_list)))

        return result_list
