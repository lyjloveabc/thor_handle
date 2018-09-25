"""
bill_sql = "INSERT INTO bill" \
           "(billing_period, gmt_create, gmt_end, gmt_modify, gmt_start, house_info_id, ought_amount, product_id, " \
           "product_type_code, product_type_id, status, title, zone_id, is_checked, financial_income, sub_period_id) " \
           "VALUES ()"

"""
import requests

spIdList = [
    94,
    95,
    96,
    97,
    98,
    99,
    100,
    101,
    102,
    103,
    104,
    105,
    106,
    107,
    169
]
spIdListStr = list()
for sp in spIdList:
    spIdListStr.append(str(sp))
spIds = ",".join(spIdListStr)
url = "http://newcloud.itianluo.cn/external/cb?token=d43b24c4a103464c887605727a6c2031&parkingId={parkingId}&subscriptionId={subscriptionId}&spIdStr={spIdStr}&operatorId=431"
with open('车位id.txt', 'r') as f:
    for row in f.readlines():
        parkingId = row.replace('\n', '')
        r = requests.get(url.format(parkingId=parkingId, subscriptionId=33, spIdStr=spIds))
        print(r)

"""
update bill
left join itl_parking_bill on itl_parking_bill.bill_id = bill.id
set bill.is_checked = 1
where bill.zone_id = 2 and bill.product_type_id = 27 and bill.is_checked = 0
and itl_parking_bill.parking_id in (673,674,712,713,725,726,727,728,729,730,731,732,733,734,739,754,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,839,1013,848,849,850,851,852,853,854,885,893,895,908,917,918,951)
and bill.gmt_start >= '2017-10-01' and bill.gmt_start <= '2018-10-01';
"""