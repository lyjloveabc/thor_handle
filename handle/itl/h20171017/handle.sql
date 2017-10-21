UPDATE bill
SET is_part_paid = 1
WHERE zone_id = 2 AND product_type_id = 27
      AND pay_flow != '' AND remark = '车位收费上线之前，已线下收费[当前特殊月处理]，没有支付流水';


UPDATE bill
SET is_checked = 0
WHERE zone_id = 2 AND product_type_id = 27
      AND gmt_start > '2018-04-30 23:59:59' AND payment_ids = '';


UPDATE bill
SET is_checked = 0
WHERE zone_id = 2 AND product_type_id = 27
      AND payment_ids = '';

# 打开2018-04之前的账单
UPDATE bill
SET is_checked = 1
WHERE zone_id = 2 AND product_type_id = 27
      AND gmt_start < '2018-05-01 00:00:00';

# 打开2018-04以后所有已支付或部分支付的账单

