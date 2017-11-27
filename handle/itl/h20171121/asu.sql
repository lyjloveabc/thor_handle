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

COMMIT;