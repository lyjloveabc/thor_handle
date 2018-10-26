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
VALUES ({b_id}, '{p_name}', now(), now(), "{gmt_start}"," {gmt_end}", {ought_amount}, 40, 'retailProperty', 28, 0, 'NO_PAY', '{pre} 商铺物业费 {title}', 76, 1, {financial_income}, {p_id});
INSERT INTO itl_business_bill (id, created_time, modified_time, zone_id, business_id, bill_id, type, last_operator)
VALUES ({biz_id}, now(), now(), 76, {s_id}, {b_id}, 'STORE', 999999999);
"""

field_index = {
    's_id': 0,
    'money': 2,
}

file_name = '天水.xlsx'
data = ReadUtil.read_file(file_name, field_index)

b_id = 478026
biz_id = 24257
p_name = [
    {'n': '商铺物业费 2017年12月', 'p': 382, 'start': '2017-12-01', 'end': '2017-12-31'},
    {'n': '商铺物业费 2018年01月', 'p': 383, 'start': '2018-01-01', 'end': '2018-01-31'},
    {'n': '商铺物业费 2018年02月', 'p': 384, 'start': '2018-02-01', 'end': '2018-02-28'},
    {'n': '商铺物业费 2018年03月', 'p': 385, 'start': '2018-03-01', 'end': '2018-03-31'},
    {'n': '商铺物业费 2018年04月', 'p': 386, 'start': '2018-04-01', 'end': '2018-04-30'},
    {'n': '商铺物业费 2018年05月', 'p': 387, 'start': '2018-05-01', 'end': '2018-05-31'},
    {'n': '商铺物业费 2018年06月', 'p': 388, 'start': '2018-06-01', 'end': '2018-06-30'},
    {'n': '商铺物业费 2018年07月', 'p': 389, 'start': '2018-07-01', 'end': '2018-07-31'},
    {'n': '商铺物业费 2018年08月', 'p': 390, 'start': '2018-08-01', 'end': '2018-08-31'},
    {'n': '商铺物业费 2018年09月', 'p': 391, 'start': '2018-09-01', 'end': '2018-09-30'},
    {'n': '商铺物业费 2018年10月', 'p': 392, 'start': '2018-10-01', 'end': '2018-10-31'},
    {'n': '商铺物业费 2018年11月', 'p': 393, 'start': '2018-11-01', 'end': '2018-11-30'},
]
p_id = 382

sssss = dict()
with open('hahahahha.txt', 'r') as f:
    for row in f.readlines():
        row = row.replace('\n', '')
        aa = row.split(',')
        sssss[aa[0]] = aa[1]

for row in data:
    for pn in p_name:
        print(
            sql.format(
                b_id=b_id,
                gmt_start=pn['start'],
                gmt_end=pn['end'],
                p_name=pn['n'],
                ought_amount=row['money'],
                pre=sssss[str(int(float(row['s_id'])))],
                title=pn['n'],
                financial_income=row['money'],
                biz_id=biz_id, s_id=row['s_id'],
                p_id=pn['p'],
            )
        )
        b_id += 1
        biz_id += 1
