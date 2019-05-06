SELECT
  bill.id                             AS id,
  IFNULL(bill.discount_money, 0)      AS discount_money,
  IFNULL(bill.financial_income, 0)    AS financial_income,
  IFNULL(bill.hang_up_bill_amount, 0) AS hang_up_bill_amount,
  IFNULL(bill.ought_amount, 0)        AS ought_amount,
  IFNULL(bill.real_amount, 0)         AS real_amount
FROM bill
WHERE
  zone_id IN (SELECT id
              FROM zones
              WHERE company_id = 1)
  AND (IFNULL(real_amount, 0) + IFNULL(discount_money, 0) + IFNULL(hang_up_bill_amount, 0)) > 0;