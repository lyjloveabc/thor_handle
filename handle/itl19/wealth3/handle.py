from utils.file.excel.readUtil import ReadUtil

file_name = 'file/需要订正的账单.xlsx'
data = ReadUtil.read_file(
    file_name,
    {'id': 0, 'ought_amount': 8, 'real_amount': 9, 'discount_amount': 10, 'round_amount': 11, 'owe_amount': 12}
)

sql = 'UPDATE itl_finance_bill ' \
      'SET ought_amount = {ought_amount}, real_amount = {real_amount}, discount_amount = {discount_amount}, round_amount = {round_amount}, owe_amount = {owe_amount} ' \
      'WHERE id = {id};'

with open(file_name + '.txt', 'a') as f:
    for row in data:
        f.write(
            sql.format(
                ought_amount=row['ought_amount'], real_amount=row['real_amount'],
                discount_amount=row['discount_amount'], round_amount=row['round_amount'],
                owe_amount=row['owe_amount']
                , id=row['id']
            )
            + '\n'
        )
