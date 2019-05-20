sql = 'UPDATE itl_finance_bill SET real_amount = ought_amount, owe_amount = 0 WHERE id = {id};'
ids = [
    "260218",
    "260725",
    "261232",
    "261739",
    "262246",
    "262753",
    "263260",
    "263767"
]

for row in ids:
    print(sql.format(id=row))
