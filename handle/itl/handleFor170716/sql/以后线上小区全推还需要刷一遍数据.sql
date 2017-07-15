## 更新现有小区的公司名称

## 所有的人员更新公司
UPDATE user LEFT JOIN zones ON zones.id = user.zone_id SET user.company_id = zones.company_id;

## 所有老校区的账单更新字段
UPDATE bill SET is_checked=1, financial_income=ought_amount WHERE zone_id in ();

## 所有业务更新user_id
UPDATE subscription_enter
LEFT JOIN admin_employee ON admin_employee.id = subscription_enter.admin_employee_id
LEFT JOIN user ON user.account = admin_employee.mobile
SET user_id=IFNULL(user.id, 0);

UPDATE task
LEFT JOIN admin_employee ON admin_employee.id = task.employee_id
LEFT JOIN user ON user.account = admin_employee.mobile
SET user_id=IFNULL(user.id, 0);