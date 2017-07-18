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

UPDATE task_map
LEFT JOIN admin_employee ON admin_employee.id = task_map.uid
LEFT JOIN user ON user.account = admin_employee.mobile
SET user_id=IFNULL(user.id, 0);

UPDATE appraisal
LEFT JOIN admin_employee ON admin_employee.id = appraisal.eid
LEFT JOIN user ON user.account = admin_employee.mobile
SET user_id=IFNULL(user.id, 0);

UPDATE appraisal_emp
LEFT JOIN admin_employee ON admin_employee.id = appraisal_emp.eid
LEFT JOIN user ON user.account = admin_employee.mobile
SET user_id=IFNULL(user.id, 0);

UPDATE appraisal_progress
LEFT JOIN admin_employee ON admin_employee.id = appraisal_progress.eid
LEFT JOIN user ON user.account = admin_employee.mobile
SET user_id=IFNULL(user.id, 0);

UPDATE appraisal_adjust
LEFT JOIN admin_employee ON admin_employee.id = appraisal_adjust.eid
LEFT JOIN user ON user.account = admin_employee.mobile
SET user_id=IFNULL(user.id, 0);

UPDATE appraisal_assignee
LEFT JOIN admin_employee ON admin_employee.id = appraisal_assignee.eid
LEFT JOIN user ON user.account = admin_employee.mobile
SET user_id=IFNULL(user.id, 0);

UPDATE summary_plan
LEFT JOIN admin_employee ON admin_employee.id = summary_plan.employee_id
LEFT JOIN user ON user.account = admin_employee.mobile
SET user_id=IFNULL(user.id, 0);

UPDATE bug_report
LEFT JOIN admin_employee ON admin_employee.id = bug_report.uid
LEFT JOIN user ON user.account = admin_employee.mobile
SET user_id=IFNULL(user.id, 0);

UPDATE chat
LEFT JOIN admin_employee ON admin_employee.id = chat.reply_id
LEFT JOIN user ON user.account = admin_employee.mobile
SET reply_id=IFNULL(user.id, 0);
