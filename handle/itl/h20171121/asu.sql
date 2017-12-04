BEGIN;


SELECT *
FROM bill
WHERE id IN
      (SELECT `bill_id`
       FROM `itl_parking_bill`
       WHERE 1 AND `parking_id` = (SELECT id
                                   FROM itl_parking
                                   WHERE zone_id = 2 AND name = '6-37')
      )
      AND `gmt_start` < '2018-11-01 00:00:00';

SELECT *
FROM bill
WHERE id IN
      (SELECT `bill_id`
       FROM `itl_parking_bill`
       WHERE 1 AND `parking_id` = (SELECT id
                                   FROM itl_parking
                                   WHERE zone_id = 2 AND name = '6-22')
      )
      AND `gmt_start` < '2018-11-01 00:00:00';

SELECT *
FROM bill
WHERE id IN (
  SELECT bill_id
  FROM `itl_parking_bill`
  WHERE parking_id IN (SELECT id
                       FROM `itl_parking`
                       WHERE zone_id = 2 AND `name` = '7-35')
)
      AND `gmt_start` < '2018-08-01 00:00:00' AND `status` = 'NO_PAY';

UPDATE bill
SET `real_amount` = `ought_amount`, `gmt_modify` = now(), `gmt_pay` = now(), `remark` = '处理L', `status` = 'PAID', `financial_income` = 0.00
WHERE id IN (SELECT bill_id
             FROM `itl_parking_bill`
             WHERE parking_id IN (SELECT id
                                  FROM `itl_parking`
                                  WHERE zone_id = 2 AND `name` = '7-36')) AND `gmt_start` < '2018-08-01 00:00:00' AND `status` = 'NO_PAY';



COMMIT;