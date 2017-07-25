## 账单、新USER_ID、公司、职能、
## 岗位、部门
## 更新现有小区的公司名称
UPDATE zones SET company_id = "11" WHERE id = "1";
UPDATE zones SET company_id = "1" WHERE id = "2";
UPDATE zones SET company_id = "13" WHERE id = "5";
UPDATE zones SET company_id = "9" WHERE id = "9";
UPDATE zones SET company_id = "8" WHERE id = "10";
UPDATE zones SET company_id = "12" WHERE id = "11";
UPDATE zones SET company_id = "12" WHERE id = "12";
UPDATE zones SET company_id = "10" WHERE id = "13";
UPDATE zones SET company_id = "10" WHERE id = "14";
UPDATE zones SET company_id = "10" WHERE id = "15";
UPDATE zones SET company_id = "10" WHERE id = "16";
UPDATE zones SET company_id = "10" WHERE id = "17";
UPDATE zones SET company_id = "6" WHERE id = "18";
UPDATE zones SET company_id = "9" WHERE id = "19";
UPDATE zones SET company_id = "12" WHERE id = "20";
UPDATE zones SET company_id = "3" WHERE id = "21";
UPDATE zones SET company_id = "3" WHERE id = "22";
UPDATE zones SET company_id = "7" WHERE id = "23";
UPDATE zones SET company_id = "2" WHERE id = "24";
UPDATE zones SET company_id = "4" WHERE id = "25";
UPDATE zones SET company_id = "4" WHERE id = "26";
UPDATE zones SET company_id = "4" WHERE id = "27";
UPDATE zones SET company_id = "5" WHERE id = "28";
UPDATE zones SET company_id = "9" WHERE id = "29";
UPDATE zones SET company_id = "5" WHERE id = "30";

## 所有的人员更新公司
UPDATE user LEFT JOIN zones ON zones.id = user.zone_id SET user.company_id = zones.company_id;

## 所有老小区的账单更新字段
UPDATE bill SET is_checked=1, financial_income=ought_amount where zone_id <= 30;

## 所有业务更新user_id
UPDATE subscription_enter
  LEFT JOIN admin_employee ON admin_employee.id = subscription_enter.admin_employee_id
  LEFT JOIN user ON user.account = admin_employee.mobile
SET user_id = IFNULL(user.id, 0)
WHERE subscription_enter.zone_id <= 30;

UPDATE task
  LEFT JOIN admin_employee ON admin_employee.id = task.employee_id
  LEFT JOIN user ON user.account = admin_employee.mobile
SET user_id = IFNULL(user.id, 0)
WHERE task.zone_id <= 30;

UPDATE task_map
  LEFT JOIN admin_employee ON admin_employee.id = task_map.uid
  LEFT JOIN user ON user.account = admin_employee.mobile
SET user_id = IFNULL(user.id, 0)
WHERE task_map.user_id = 0;

UPDATE appraisal
  LEFT JOIN admin_employee ON admin_employee.id = appraisal.eid
  LEFT JOIN user ON user.account = admin_employee.mobile
SET user_id = IFNULL(user.id, 0)
WHERE appraisal.zone_id <= 30;

UPDATE appraisal_emp
  LEFT JOIN admin_employee ON admin_employee.id = appraisal_emp.eid
  LEFT JOIN user ON user.account = admin_employee.mobile
SET user_id = IFNULL(user.id, 0)
WHERE appraisal_emp.user_id = 0;

UPDATE appraisal_progress
  LEFT JOIN admin_employee ON admin_employee.id = appraisal_progress.eid
  LEFT JOIN user ON user.account = admin_employee.mobile
SET user_id = IFNULL(user.id, 0)
WHERE appraisal_progress.user_id = 0;

UPDATE appraisal_adjust
  LEFT JOIN admin_employee ON admin_employee.id = appraisal_adjust.eid
  LEFT JOIN user ON user.account = admin_employee.mobile
SET user_id = IFNULL(user.id, 0)
WHERE appraisal_adjust.user_id = 0;

UPDATE appraisal_assignee
  LEFT JOIN admin_employee ON admin_employee.id = appraisal_assignee.eid
  LEFT JOIN user ON user.account = admin_employee.mobile
SET user_id = IFNULL(user.id, 0)
WHERE appraisal_assignee.user_id = 0;

UPDATE summary_plan
  LEFT JOIN admin_employee ON admin_employee.id = summary_plan.employee_id
  LEFT JOIN user ON user.account = admin_employee.mobile
SET user_id = IFNULL(user.id, 0)
WHERE summary_plan.zone_id <= 30;

UPDATE bug_report
LEFT JOIN admin_employee ON admin_employee.id = bug_report.uid
LEFT JOIN user ON user.account = admin_employee.mobile
SET user_id=IFNULL(user.id, 0);

UPDATE chat
  LEFT JOIN admin_employee ON admin_employee.id = chat.reply_id
  LEFT JOIN user ON user.account = admin_employee.mobile
SET reply_id = IFNULL(user.id, 0)
WHERE chat.zone_id <= 30;
