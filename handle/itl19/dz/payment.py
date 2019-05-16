from utils.file.excel.readUtil import ReadUtil

sql_update = 'UPDATE itl_finance_payment SET' \
             ' gmt_create = "{gmt_create}",' \
             ' gmt_modified = "{gmt_modified}",' \
             ' zone_id = "{zone_id}",' \
             ' amount = "{amount}",' \
             ' pay_time = "{pay_time}",' \
             ' pay_title = "{pay_title}",' \
             ' payment_channel = "{payment_channel}",' \
             ' uuid = "{uuid}",' \
             ' trade_no = "{trade_no}",' \
             ' payer_owner_id = "{payer_owner_id}",' \
             ' receiver_id = "{receiver_id}",' \
             ' charge_object_type = "{charge_object_type}",' \
             ' charge_object_value = "{charge_object_value}",' \
             ' contact_number = "{contact_number}",' \
             ' remark = "{remark}",' \
             ' has_refund = "{has_refund}",' \
             ' is_garbage = "{is_garbage}",' \
             ' number_condition = "{number_condition}"' \
             ' WHERE id ={id};'
data = ReadUtil.read_file('file/要调账的数据（小罗要的格式）.xlsx', {
    'id': 0,
    'gmt_create': 1,
    'gmt_modified': 2,
    'zone_id': 3,
    'amount': 4,
    'pay_time': 5,
    'pay_title': 6,
    'payment_channel': 7,
    'uuid': 8,
    'trade_no': 9,
    'payer_owner_id': 10,
    'receiver_id': 11,
    'charge_object_type': 12,
    'charge_object_value': 13,
    'contact_number': 14,
    'remark': 15,
    'has_refund': 16,
    'is_garbage': 17,
    'number_condition': 18,
})

print()
print()
print()
for row in data:
    print(
        sql_update.format(
            id=row['id'],
            gmt_create=row['gmt_create'],
            gmt_modified=row['gmt_modified'],
            zone_id=row['zone_id'],
            amount=row['amount'],
            pay_time=row['pay_time'],
            pay_title=row['pay_title'],
            payment_channel=row['payment_channel'],
            uuid=row['uuid'],
            trade_no=row['trade_no'],
            payer_owner_id=row['payer_owner_id'],
            receiver_id=row['receiver_id'],
            charge_object_type=row['charge_object_type'],
            charge_object_value=row['charge_object_value'],
            contact_number=row['contact_number'],
            remark=row['remark'],
            has_refund=row['has_refund'],
            is_garbage=row['is_garbage'],
            number_condition=row['number_condition'],
        )
    )

print()
print()
