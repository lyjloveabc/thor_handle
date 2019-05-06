SELECT
  bill.id             oldId,
  itl_finance_bill.id newId,
  itl_finance_bill.ought_amount
FROM itl_finance_bill
  INNER JOIN bill ON date_format(bill.gmt_start, '%Y%m') = date_format(itl_finance_bill.start_day, '%Y%m')
WHERE
  itl_finance_bill.subject_id IN (2, 5, 7, 38, 47)
  AND bill.product_type_id IN (2, 5, 7, 38, 47)
  AND itl_finance_bill.subject_id = bill.product_type_id
  AND itl_finance_bill.zone_id = bill.zone_id
  AND itl_finance_bill.estate_id = bill.house_info_id
  AND bill.zone_id IN (SELECT id
                       FROM zones
                       WHERE company_id = 1)
  AND (ifnull(bill.real_amount, 0) + ifnull(bill.discount_money, 0) + ifnull(bill.hang_up_bill_amount, 0)) > 0
UNION ALL
SELECT
  bill.id             oldId,
  itl_finance_bill.id newId,
  itl_finance_bill.ought_amount
FROM itl_finance_bill
  INNER JOIN bill ON date_format(bill.gmt_start, '%Y%m') = date_format(itl_finance_bill.start_day, '%Y%m')
  INNER JOIN itl_business_bill ON itl_business_bill.type = 'STORE' AND bill.id = itl_business_bill.bill_id
WHERE
  itl_finance_bill.subject_id IN (28, 39, 48)
  AND bill.product_type_id IN (28, 39, 48)
  AND itl_finance_bill.subject_id = bill.product_type_id
  AND itl_finance_bill.zone_id = bill.zone_id
  AND itl_finance_bill.estate_id = itl_business_bill.business_id
  AND bill.zone_id IN (SELECT id
                       FROM zones
                       WHERE company_id = 1)
  AND (ifnull(bill.real_amount, 0) + ifnull(bill.discount_money, 0) + ifnull(bill.hang_up_bill_amount, 0)) > 0
UNION ALL
SELECT
  bill.id             oldId,
  itl_finance_bill.id newId,
  itl_finance_bill.ought_amount
FROM itl_finance_bill
  INNER JOIN bill ON date_format(bill.gmt_start, '%Y%m') = date_format(itl_finance_bill.start_day, '%Y%m')
  INNER JOIN itl_parking_bill ON itl_parking_bill.bill_id = bill.id
WHERE
  itl_finance_bill.subject_id = 27
  AND bill.product_type_id = 27
  AND itl_finance_bill.zone_id = bill.zone_id
  AND itl_finance_bill.estate_id = itl_parking_bill.parking_id
  AND bill.zone_id IN (SELECT id
                       FROM zones
                       WHERE company_id = 1)
  AND (ifnull(bill.real_amount, 0) + ifnull(bill.discount_money, 0) + ifnull(bill.hang_up_bill_amount, 0)) > 0
UNION ALL
SELECT
  bill.id             oldId,
  itl_finance_bill.id newId,
  itl_finance_bill.ought_amount
FROM itl_finance_bill
  INNER JOIN bill ON date_format(bill.gmt_start, '%Y%m') = date_format(itl_finance_bill.start_day, '%Y%m')
  INNER JOIN itl_business_bill ON itl_business_bill.type = 'SHOP' AND bill.id = itl_business_bill.bill_id
WHERE
  itl_finance_bill.subject_id IN (34, 35)
  AND bill.product_type_id IN (34, 35)
  AND itl_finance_bill.subject_id = bill.product_type_id
  AND itl_finance_bill.zone_id = bill.zone_id
  AND itl_finance_bill.estate_id = itl_business_bill.business_id
  AND bill.zone_id IN (SELECT id
                       FROM zones
                       WHERE company_id = 1)
  AND (ifnull(bill.real_amount, 0) + ifnull(bill.discount_money, 0) + ifnull(bill.hang_up_bill_amount, 0)) > 0;
