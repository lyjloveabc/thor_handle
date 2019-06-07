from utils.file.excel.readUtil import ReadUtil

file_name = 'file/绿都商铺数据调整.xlsx'
data = ReadUtil.read_file(file_name, {'id': 2, 'amount': 5})

sql = 'UPDATE itl_finance_bill SET ought_amount = {ought_amount}, owe_amount = {owe_amount} WHERE id = {id};'

with open(file_name + '.txt', 'a') as f:
    for row in data:
        f.write(
            sql.format(ought_amount=row['amount'], owe_amount=row['amount'], id=row['id']) + '\n'
        )
