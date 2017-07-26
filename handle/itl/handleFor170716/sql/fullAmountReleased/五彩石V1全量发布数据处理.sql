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

# 更新老角色到新角色
UPDATE user_role_relation SET role_code = '第一权限管理员' WHERE role_code = 'firstPermissionSystemAdmin';
UPDATE user_role_relation SET role_code = '项目负责人' WHERE role_code = 'projectManager';
UPDATE user_role_relation SET role_code = '客服负责人' WHERE role_code = 'customerServiceManager';
UPDATE user_role_relation SET role_code = '保洁负责人' WHERE role_code = 'cleanerManager';
UPDATE user_role_relation SET role_code = '保洁' WHERE role_code = 'cleaner';
UPDATE user_role_relation SET role_code = '绿化负责人' WHERE role_code = 'gardenerManager';
UPDATE user_role_relation SET role_code = '绿化' WHERE role_code = 'gardener';
UPDATE user_role_relation SET role_code = '保安负责人' WHERE role_code = 'securityManager';
UPDATE user_role_relation SET role_code = '门岗' WHERE role_code = 'gateSentry';
UPDATE user_role_relation SET role_code = '巡逻岗' WHERE role_code = 'patrolPost';
UPDATE user_role_relation SET role_code = '监控岗' WHERE role_code = 'monitoringPost';
UPDATE user_role_relation SET role_code = '车库岗' WHERE role_code = 'carportSecurity';
UPDATE user_role_relation SET role_code = '工程负责人' WHERE role_code = 'engineeringManager';
UPDATE user_role_relation SET role_code = '工程' WHERE role_code = 'maintainer';
UPDATE user_role_relation SET role_code = '外部维修商' WHERE role_code = 'outsideMaintainer';
UPDATE user_role_relation SET role_code = '财务' WHERE role_code = 'subFinance';
UPDATE user_role_relation SET role_code = '外围观测者' WHERE role_code = 'schrodinger';
UPDATE user_role_relation SET role_code = '苹果审核专用' WHERE role_code = 'toAppStore';
UPDATE user_role_relation SET role_code = '巡更' WHERE role_code = 'patrolExecutive';
UPDATE user_role_relation SET role_code = '业委会' WHERE role_code = 'industry Committee';
UPDATE user_role_relation SET role_code = '管家客服' WHERE role_code = 'customerService';

# 新增以前的客服为前台客服
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '24', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '44', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '57', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '59', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '61', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '71', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '77', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '82', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '104', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '112', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '114', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '192', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '223', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '235', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '253', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '268', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '283', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '285', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '309', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '319', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '401', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '405', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '499', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '571', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '620', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '671', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '680', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '710', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '717', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '723', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '724', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '763', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '770', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '791', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '793', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '821', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '831', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '854', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '870', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '897', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '925', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '933', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '937', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '938', '前台客服');
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), '939', '前台客服');

# 删除不用的角色相关关系表
DELETE FROM user_role_relation WHERE role_code IN ('jobAdjustment', 'companyManager', 'energyMeterReader', 'businessExecutive', 'liftWorker');

# 老小区的临时任务处理
