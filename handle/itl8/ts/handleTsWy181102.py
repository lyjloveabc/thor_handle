"""
天水的。
住宅物业费，出36个月（36个账单），2017年12-2018年11月的，审核，另外不审核；
住宅公共维修费，出3年（3个账单），第一年的审核，其他不审核
住宅能耗费，出1年，审核

select
id, period_name, date_format(period_start, '%Y-%m-%d'), date_format(period_end, '%Y-%m-%d')
from subscription_period where zone_id = 76 and product_id = 43;

select id, house, building, door from house_info
where
(house = 15 and building = 47 and door = 209)
or (house = 15 and building = 47 and door = 210)
or (house = 39 and building = 114 and door = 210)
or (house = 39 and building = 116 and door = 205);
"""

from utils.file.excel.readUtil import ReadUtil

sql = """
INSERT INTO bill (id,
                  billing_period,
                  gmt_create,
                  gmt_modify,
                  gmt_start,
                  gmt_end,
                  house_info_id,
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
VALUES 
({b_id}, '{p_name}', now(), now(), "{start}"," {end}", {house_info_id}, {ought_amount}, 43, 'propertyFee', 7, NULL, 'NO_PAY', '{title}', 76, {is_checked}, {financial_income}, {p_id});
"""

data = ReadUtil.read_file(
    '物业用房账单明细_data.xls',
    {
        'id': 0,
        'house': 1,
        'building': 2,
        'door': 3,
        'wyf': 8,
        'ggf': 9,
        'nhf': 10,
    }
)

sp = list()
with open('wyf_p.txt', 'r') as f:
    for line in f.readlines():
        d = line.replace('\n', '').split(',')
        sp.append(d)

b_id = 483778
for row in data:
    for p in sp:
        print(
            sql.format(
                b_id=b_id,
                p_name=p[1],
                start=p[2],
                end=p[3],
                house_info_id=row['id'],
                ought_amount=row['wyf'],
                title=row['house'] + "-" + row['building'] + "-" + row['door'] + " " + p[1],
                is_checked=(1 if int(p[0]) <= 156 else 0),
                financial_income=row['wyf'],
                p_id=p[0],
            )
        )
        b_id += 1
