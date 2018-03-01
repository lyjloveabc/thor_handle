"""
select
itl_parking.name, bill.id, date_format(bill.gmt_start, '%m')
from itl_parking
left join itl_parking_bill on itl_parking_bill.parking_id = itl_parking.id
left join bill on bill.id = itl_parking_bill.bill_id
where itl_parking.zone_id = 82 and bill.gmt_start >= '2018-01-01'
order by itl_parking.name;
"""
from utils.constant.constant import Constant

sql = 'UPDATE bill SET real_amount = "{real_amount}", financial_income = "{financial_income}", status = "{status}", is_part_paid = "{is_part_paid}" WHERE id = "{id}";'
db = dict()

with open('file/zd_parking_bill.txt', 'r') as f:
    for row in f.readlines():
        data = row.split(',')
        db[data[0] + '-' + str(int(data[2]))] = data[1]

result = list()

with open('file/浙地车位账单调整.txt', 'r') as f:
    for row in f.readlines():
        if row == '':
            continue
        index = 1
        data = row.replace('\n', '').replace(' ', '').split(',')

        while index <= 12:
            key = data[0] + '-' + str(index)

            if key in db:
                financial_income = 50.00 - float(data[index])

                result.append(
                    sql.format(real_amount=data[index], financial_income=financial_income,
                               status='PAID' if financial_income <= 0 else 'NO_PAY',
                               is_part_paid='0' if financial_income <= 0 else '1',
                               id=db[key])
                )
            index += 1

with open('file/浙地车位账单调整_out.txt', 'a') as f:
    f.write(Constant.SQL_BEGIN)
    f.write('\n')
    for row in result:
        f.write(row)
        f.write('\n')
    f.write(Constant.SQL_COMMIT)


# for k, v in db.items():
#     print(k, v)
