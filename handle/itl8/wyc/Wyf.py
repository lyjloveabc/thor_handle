"""
select id, house, building, door from house_info where zone_id = 24;

select id, period_start from subscription_period
where zone_id = 24 and product_id = 24 and id > 161;
"""
from utils.file.excel.readUtil import ReadUtil

# 改造战斗感金额的sql
sql = 'UPDATE bill ' \
      'SET title = {title}, ought_amount = {ought_amount}, gmt_modify = now(), remark="手动处理", financial_income = {financial_income} ' \
      'WHERE zone_id = 24 AND sub_period_id = {sub_period_id} AND house_info_id = {house_info_id};'

# 原始数据
data = ReadUtil.read_file('万源城逸郡2019年账单导入.xlsx', {'title': 2, 'house_name': 3, 'ought_amount': 4, 'financial_income': 5})

# 万源城的房号数据
house_info = dict()
with open('wycHouse.txt', 'r') as f:
    for row in f.readlines():
        hd = row.replace('\n', '').split(',')
        key = hd[1] + '幢' + hd[2] + '单元' + str(int(hd[3])) + '室'
        house_info[key] = hd[0]

# 账单对应账期
bill_period = {
    '01/01/2019': '物业费+车位管理费2019年1月-3月',
    '04/01/2019': '物业费+车位管理费2019年4月-6月',
    '07/01/2019': '物业费+车位管理费2019年7月-9月',
    '10/01/2019': '物业费+车位管理费2019年10月-12月'
}
# 万源城物业费的账期
sub_period = dict()
with open('wycSubPeriod.txt', 'r') as f:
    for row in f.readlines():
        sb = row.replace('\n', '').split(',')
        sub_period[bill_period[sb[1]]] = sb[0]

for row in data:
    print(
        sql.format(
            title=row['title'],
            ought_amount=row['ought_amount'] if row['ought_amount'] != '' else 0,
            financial_income=row['financial_income'] if row['financial_income'] != '' else 0,
            sub_period_id=sub_period[row['title']],
            house_info_id=house_info[row['house_name']]
        )
    )
