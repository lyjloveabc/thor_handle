# 2017-10-24

# 8-3  毛梦丹 208 859
# 9-19 张敏儿 473 946

# 补充能耗数据
INSERT INTO subscription_enter
(id, zone_id, sub_id, house_info_id, bill_id, name, product_type_code, gmt_create, gmt_modify, detail, status, hasbill, admin_employee_id, period_id, user_id)
VALUES
  (17992, 2, 33, 208, 0, '车位费 2017年10月', 'parking', now(), now(), '{"unitPrice":40.0}', 'NO_ENTER', 'BILL', NULL, 94, 431),
  (17993, 2, 33, 208, 0, '车位费 2017年11月', 'parking', now(), now(), '{"unitPrice":40.0}', 'NO_ENTER', 'BILL', NULL, 95, 431),
  (17994, 2, 33, 208, 0, '车位费 2017年12月', 'parking', now(), now(), '{"unitPrice":40.0}', 'NO_ENTER', 'BILL', NULL, 96, 431),
  (17995, 2, 33, 208, 0, '车位费 2018年01月', 'parking', now(), now(), '{"unitPrice":40.0}', 'NO_ENTER', 'BILL', NULL, 97, 431),
  (17996, 2, 33, 208, 0, '车位费 2018年02月', 'parking', now(), now(), '{"unitPrice":40.0}', 'NO_ENTER', 'BILL', NULL, 98, 431),
  (17997, 2, 33, 208, 0, '车位费 2018年03月', 'parking', now(), now(), '{"unitPrice":40.0}', 'NO_ENTER', 'BILL', NULL, 99, 431),
  (17998, 2, 33, 208, 0, '车位费 2018年04月', 'parking', now(), now(), '{"unitPrice":40.0}', 'NO_ENTER', 'BILL', NULL, 100, 431),

  (17999, 2, 33, 473, 0, '车位费 2017年12月', 'parking', now(), now(), '{"unitPrice":40.0}', 'NO_ENTER', 'BILL', NULL, 96, 431),
  (18000, 2, 33, 473, 0, '车位费 2018年01月', 'parking', now(), now(), '{"unitPrice":40.0}', 'NO_ENTER', 'BILL', NULL, 97, 431),
  (18001, 2, 33, 473, 0, '车位费 2018年02月', 'parking', now(), now(), '{"unitPrice":40.0}', 'NO_ENTER', 'BILL', NULL, 98, 431),
  (18002, 2, 33, 473, 0, '车位费 2018年03月', 'parking', now(), now(), '{"unitPrice":40.0}', 'NO_ENTER', 'BILL', NULL, 99, 431),
  (18003, 2, 33, 473, 0, '车位费 2018年04月', 'parking', now(), now(), '{"unitPrice":40.0}', 'NO_ENTER', 'BILL', NULL, 100, 431);

# 补充车位账单数据
INSERT INTO bill
(id, zone_id, house_info_id, uid, title, product_type_id, product_type_code, product_id, sub_enter_id, billing_period, payment_id, ought_amount, real_amount,
 gmt_start, gmt_end, gmt_create, gmt_modify, gmt_pay, bill_adjust_log_id, remark, status, discount_num, discount_money, is_checked, financial_income,
 approval_id, pay_flow, payment_ids, is_part_paid)
VALUES
  (16564, 2, 208, 0, '车位费 2017年10月', 27, 'parking', 33, 17992, '车位费 2017年10月', NULL, 40.00, NULL, '2017-10-01', '2017-10-31', now(), now(), NULL, NULL,
                                                                                     '公共转私家，补的账单', 'NO_PAY', NULL, 0.00, 1, 40.00, NULL, '', '', 0),
  (16565, 2, 208, 0, '车位费 2017年11月', 27, 'parking', 33, 17993, '车位费 2017年11月', NULL, 40.00, NULL, '2017-11-01', '2017-11-30', now(), now(), NULL, NULL,
                                                                                     '公共转私家，补的账单', 'NO_PAY', NULL, 0.00, 1, 40.00, NULL, '', '', 0),
  (16566, 2, 208, 0, '车位费 2017年12月', 27, 'parking', 33, 17994, '车位费 2017年12月', NULL, 40.00, NULL, '2017-12-01', '2017-12-31', now(), now(), NULL, NULL,
                                                                                     '公共转私家，补的账单', 'NO_PAY', NULL, 0.00, 1, 40.00, NULL, '', '', 0),
  (16567, 2, 208, 0, '车位费 2018年01月', 27, 'parking', 33, 17995, '车位费 2018年01月', NULL, 40.00, NULL, '2018-01-01', '2018-01-31', now(), now(), NULL, NULL,
                                                                                     '公共转私家，补的账单', 'NO_PAY', NULL, 0.00, 1, 40.00, NULL, '', '', 0),
  (16568, 2, 208, 0, '车位费 2018年02月', 27, 'parking', 33, 17996, '车位费 2018年02月', NULL, 40.00, NULL, '2018-02-01', '2018-02-28', now(), now(), NULL, NULL,
                                                                                     '公共转私家，补的账单', 'NO_PAY', NULL, 0.00, 1, 40.00, NULL, '', '', 0),
  (16569, 2, 208, 0, '车位费 2018年03月', 27, 'parking', 33, 17997, '车位费 2018年03月', NULL, 40.00, NULL, '2018-03-01', '2018-03-31', now(), now(), NULL, NULL,
                                                                                     '公共转私家，补的账单', 'NO_PAY', NULL, 0.00, 1, 40.00, NULL, '', '', 0),
  (16570, 2, 208, 0, '车位费 2018年04月', 27, 'parking', 33, 17998, '车位费 2018年04月', NULL, 40.00, NULL, '2018-04-01', '2018-04-30', now(), now(), NULL, NULL,
                                                                                     '公共转私家，补的账单', 'NO_PAY', NULL, 0.00, 1, 40.00, NULL, '', '', 0),

  (16571, 2, 473, 0, '车位费 2017年12月', 27, 'parking', 33, 17999, '车位费 2017年12月', NULL, 40.00, NULL, '2017-12-01', '2017-12-31', now(), now(), NULL, NULL,
                                                                                     '公共转私家，补的账单', 'NO_PAY', NULL, 0.00, 1, 40.00, NULL, '', '', 0),
  (16572, 2, 473, 0, '车位费 2018年01月', 27, 'parking', 33, 18000, '车位费 2018年01月', NULL, 40.00, NULL, '2018-01-01', '2018-01-31', now(), now(), NULL, NULL,
                                                                                     '公共转私家，补的账单', 'NO_PAY', NULL, 0.00, 1, 40.00, NULL, '', '', 0),
  (16573, 2, 473, 0, '车位费 2018年02月', 27, 'parking', 33, 18001, '车位费 2018年02月', NULL, 40.00, NULL, '2018-02-01', '2018-02-28', now(), now(), NULL, NULL,
                                                                                     '公共转私家，补的账单', 'NO_PAY', NULL, 0.00, 1, 40.00, NULL, '', '', 0),
  (16574, 2, 473, 0, '车位费 2018年03月', 27, 'parking', 33, 18002, '车位费 2018年03月', NULL, 40.00, NULL, '2018-03-01', '2018-03-31', now(), now(), NULL, NULL,
                                                                                     '公共转私家，补的账单', 'NO_PAY', NULL, 0.00, 1, 40.00, NULL, '', '', 0),
  (16575, 2, 473, 0, '车位费 2018年04月', 27, 'parking', 33, 18003, '车位费 2018年04月', NULL, 40.00, NULL, '2018-04-01', '2018-04-30', now(), now(), NULL, NULL,
                                                                                     '公共转私家，补的账单', 'NO_PAY', NULL, 0.00, 1, 40.00, NULL, '', '', 0);

# 补充车位账单关联表数据
INSERT INTO itl_parking_bill
(id, created_time, modified_time, zone_id, parking_id, bill_id, last_operator)
VALUES
  (5211, now(), now(), 2, 859, 16564, 431),
  (5212, now(), now(), 2, 859, 16565, 431),
  (5213, now(), now(), 2, 859, 16566, 431),
  (5214, now(), now(), 2, 859, 16567, 431),
  (5215, now(), now(), 2, 859, 16568, 431),
  (5216, now(), now(), 2, 859, 16569, 431),
  (5217, now(), now(), 2, 859, 16570, 431),

  (5218, now(), now(), 2, 946, 16571, 431),
  (5219, now(), now(), 2, 946, 16572, 431),
  (5220, now(), now(), 2, 946, 16573, 431),
  (5221, now(), now(), 2, 946, 16574, 431),
  (5222, now(), now(), 2, 946, 16575, 431);