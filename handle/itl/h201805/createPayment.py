sql = "INSERT INTO `itl_advance_payment` VALUES ('{id}', '2018-06-08 10:58:44', '2018-06-08 10:58:45', '1', '3140', '啸天用了预付款', '10.00', '10.00', '2018-06-08 10:59:14', 'ALI_PAY_SCAN', '111', '2222', 'hahaha ', '12345rece', '431', 'PAID', NULL, '0', NULL);"

for index in range(1, 100):
    print(sql.format(id=index))
