from handle.sea.history import qqq
from utils.file.excel.excelReadUtil import ExcelReadUtil

ld = ExcelReadUtil.read_file(file_name='operate_log_all.xlsx',
                             field_index_dict={
                                 'B_DATE': 0,
                                 'S_DATE': 1,
                                 'NAME': 2,
                                 'B_PRICE': 3,
                                 'B_TOTAL': 4,
                                 'S_PRICE': 5,
                                 'S_TOTAL': 6,
                                 'NUM': 7,
                                 'PROFIT': 8,
                                 'RATE': 9,
                             },
                             pre_index_sheet=1
                             )

sql = 'insert into stock_statistic (created_time, modified_time, code, name, abbreviation, buy_date, buy_price, sold_date, sold_price, total_num, profit, profit_rate)' \
      ' values (now(), now(), "{}", "{}", "{}", {}, {}, {}, {}, {}, {}, {});'

print()
print()
print()
print()
print()
print()
print()
print()
for row in ld:
    if row['NAME'] == 'ZQETF':
        print(sql.format(
            '512880',
            '证券ETF',
            row['NAME'],
            row['B_DATE'],
            row['B_PRICE'],
            row['S_DATE'],
            row['S_PRICE'],
            row['NUM'],
            row['PROFIT'],
            row['RATE']))
    else:
        if len(qqq.qqq[row['NAME']]) > 1:
            print('------------' + str(qqq.qqq[row['NAME']]))
        print(sql.format(
            qqq.qqq[row['NAME']][0]['code'],
            qqq.qqq[row['NAME']][0]['name'],
            row['NAME'],
            row['B_DATE'],
            row['B_PRICE'],
            row['S_DATE'],
            row['S_PRICE'],
            row['NUM'],
            row['PROFIT'],
            row['RATE']))
print()
print()
print()
print()
print()
print()
print()
print()
