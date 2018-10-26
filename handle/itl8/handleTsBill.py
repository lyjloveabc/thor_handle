from utils.file.excel.readUtil import ReadUtil

sql = """
INSERT INTO bill (id,
                  billing_period,
                  gmt_create,
                  gmt_modify,
                  gmt_start,
                  gmt_end,
                  ought_amount,
                  product_id,
                  product_type_code,
                  product_type_id,
                  real_amount,
                  status,
                  title,
                  zone_id,
                  is_checked,
                  financial_income,
                  sub_period_id)
VALUES ({b_id}, '2017年12月-2018年11月', now(), now(), '2017-12-01', '2018-11-30', {ought_amount}, 45, 'shopPublicMaintenance',39, 0, 'NO_PAY', '{pre} 商铺公共维修费 2017年12月-2018年11月', 76, 1, {financial_income}, 180);
INSERT INTO itl_business_bill (id, created_time, modified_time, zone_id, business_id, bill_id, type, last_operator)
VALUES ({biz_id}, now(), now(), 76, {s_id}, {b_id}, 'STORE', 999999999);
"""

field_index = {
    's_id': 0,
    'money': 3,
}

file_name = '天水.xlsx'
data = ReadUtil.read_file(file_name, field_index)

sssss = dict()
with open('hahahahha.txt', 'r') as f:
    for row in f.readlines():
        row = row.replace('\n', '')
        aa = row.split(',')
        sssss[aa[0]] = aa[1]

b_id = 478016
biz_id = 24247

for row in data:
    print(
        sql.format(
            b_id=b_id,
            ought_amount=row['money'],
            pre=sssss[str(int(float(row['s_id'])))],
            financial_income=row['money'],
            biz_id=biz_id, s_id=row['s_id']
        )
    )
    b_id += 1
    biz_id += 1
