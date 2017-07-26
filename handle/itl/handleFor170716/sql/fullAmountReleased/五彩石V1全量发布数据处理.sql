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

# 公司管理账号、老小区管理账号建立
SET SQL_SAFE_UPDATES = 0;
START TRANSACTION;
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "GMWY0726", "aff9d3d7a4fc9b02a41515bce811282e", "公明物业-管理员", "公明物业-管理员", (SELECT id FROM itl_company WHERE company_name = "公明物业"),"", "");
UPDATE itl_company SET manager_id = (SELECT id FROM user WHERE account = "GMWY0726") WHERE company_name = "公明物业";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "GMWY0726"), "物业公司管理员");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "WYCYJ0726", "c4e7f55e2246f34bfffaf5a96f7f23e3", "万源城业委会-管理员", "万源城业委会-管理员", (SELECT id FROM itl_company WHERE company_name = "万源城业委会"),"", "");
UPDATE itl_company SET manager_id = (SELECT id FROM user WHERE account = "WYCYJ0726") WHERE company_name = "万源城业委会";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "WYCYJ0726"), "物业公司管理员");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "SQWY0726", "5aa2e1267cf50d7eef3361c9571fbeae", "盛全物业-管理员", "盛全物业-管理员", (SELECT id FROM itl_company WHERE company_name = "盛全物业"),"", "");
UPDATE itl_company SET manager_id = (SELECT id FROM user WHERE account = "SQWY0726") WHERE company_name = "盛全物业";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "SQWY0726"), "物业公司管理员");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "TJWY0726", "319b3fa98e20e60f9a74b92cf631f87c", "泰杰物业-管理员", "泰杰物业-管理员", (SELECT id FROM itl_company WHERE company_name = "泰杰物业"),"", "");
UPDATE itl_company SET manager_id = (SELECT id FROM user WHERE account = "TJWY0726") WHERE company_name = "泰杰物业";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "TJWY0726"), "物业公司管理员");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "HLWY0726", "bbd7f624596f78afd086b08b0accbf47", "华隆物业-管理员", "华隆物业-管理员", (SELECT id FROM itl_company WHERE company_name = "华隆物业"),"", "");
UPDATE itl_company SET manager_id = (SELECT id FROM user WHERE account = "HLWY0726") WHERE company_name = "华隆物业";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "HLWY0726"), "物业公司管理员");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "XYWY0726", "c18da8dc4814f8fc7089fe2e7042b3fd", "玺悦物业-管理员", "玺悦物业-管理员", (SELECT id FROM itl_company WHERE company_name = "玺悦物业"),"", "");
UPDATE itl_company SET manager_id = (SELECT id FROM user WHERE account = "XYWY0726") WHERE company_name = "玺悦物业";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "XYWY0726"), "物业公司管理员");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "KXYWY0726", "cbe255581b1da9970dadd4ed735f20a3", "凯喜雅物业-管理员", "凯喜雅物业-管理员", (SELECT id FROM itl_company WHERE company_name = "凯喜雅物业"),"", "");
UPDATE itl_company SET manager_id = (SELECT id FROM user WHERE account = "KXYWY0726") WHERE company_name = "凯喜雅物业";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "KXYWY0726"), "物业公司管理员");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "FYWY0726", "9d6d0665424970d30b3b5785bfae45fc", "泛亚物业-管理员", "泛亚物业-管理员", (SELECT id FROM itl_company WHERE company_name = "泛亚物业"),"", "");
UPDATE itl_company SET manager_id = (SELECT id FROM user WHERE account = "FYWY0726") WHERE company_name = "泛亚物业";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "FYWY0726"), "物业公司管理员");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "LYWY0726", "9c91006cba3f2329eb6a17ef8bb97310", "绿宇物业-管理员", "绿宇物业-管理员", (SELECT id FROM itl_company WHERE company_name = "绿宇物业"),"", "");
UPDATE itl_company SET manager_id = (SELECT id FROM user WHERE account = "LYWY0726") WHERE company_name = "绿宇物业";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "LYWY0726"), "物业公司管理员");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "QTWY0726", "ac825b80d500221903fac287609d0d1b", "钱塘物业-管理员", "钱塘物业-管理员", (SELECT id FROM itl_company WHERE company_name = "钱塘物业"),"", "");
UPDATE itl_company SET manager_id = (SELECT id FROM user WHERE account = "QTWY0726") WHERE company_name = "钱塘物业";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "QTWY0726"), "物业公司管理员");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "CSWY0726", "47697b6e2049db37c435ec662fe5a06e", "测试物业-管理员", "测试物业-管理员", (SELECT id FROM itl_company WHERE company_name = "测试物业"),"", "");
UPDATE itl_company SET manager_id = (SELECT id FROM user WHERE account = "CSWY0726") WHERE company_name = "测试物业";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "CSWY0726"), "物业公司管理员");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "TYWY0726", "d487307c69afa9f92f5d92d40ef932b4", "体验物业-管理员", "体验物业-管理员", (SELECT id FROM itl_company WHERE company_name = "体验物业"),"", "");
UPDATE itl_company SET manager_id = (SELECT id FROM user WHERE account = "TYWY0726") WHERE company_name = "体验物业";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "TYWY0726"), "物业公司管理员");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "LZRY0726", "96753a1273ea34db9a3496a612f566ff", "离职人员-管理员", "离职人员-管理员", (SELECT id FROM itl_company WHERE company_name = "离职人员"),"", "");
UPDATE itl_company SET manager_id = (SELECT id FROM user WHERE account = "LZRY0726") WHERE company_name = "离职人员";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "LZRY0726"), "物业公司管理员");



INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "JJY0726", "71dd0054d64c93c001c4bb2a33d76f8f", "景江苑-管理员", "景江苑-管理员", (SELECT id FROM itl_company WHERE company_name = "公明物业"),"(select id from zones where name = '景江苑')", "(select id from zones where name = '景江苑')");
UPDATE zones SET manager_id = (SELECT id FROM user WHERE account = "JJY0726") WHERE name = "景江苑";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "JJY0726"), "后台项目管理员");
INSERT INTO itl_zone_category(gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name) VALUES (now(), now(), (SELECT id FROM zones WHERE name = "景江苑"), 11, "项目部");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "YJXQ0726", "ae8efc858422d72e5e722e10e86561b7", "万源城逸郡-管理员", "万源城逸郡-管理员", (SELECT id FROM itl_company WHERE company_name = "万源城业委会"),"(select id from zones where name = '万源城逸郡')", "(select id from zones where name = '万源城逸郡')");
UPDATE zones SET manager_id = (SELECT id FROM user WHERE account = "YJXQ0726") WHERE name = "万源城逸郡";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "YJXQ0726"), "后台项目管理员");
INSERT INTO itl_zone_category(gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name) VALUES (now(), now(), (SELECT id FROM zones WHERE name = "万源城逸郡"), 11, "项目部");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "DXZY0726", "4fe72e6dc2e108fd9bd081b99f7a9cea", "德信臻园-管理员", "德信臻园-管理员", (SELECT id FROM itl_company WHERE company_name = "盛全物业"),"(select id from zones where name = '德信臻园')", "(select id from zones where name = '德信臻园')");
UPDATE zones SET manager_id = (SELECT id FROM user WHERE account = "DXZY0726") WHERE name = "德信臻园";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "DXZY0726"), "后台项目管理员");
INSERT INTO itl_zone_category(gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name) VALUES (now(), now(), (SELECT id FROM zones WHERE name = "德信臻园"), 11, "项目部");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "BHGY0726", "9f3241b5874783ef47d9c6cf31bcb262", "北海公园-管理员", "北海公园-管理员", (SELECT id FROM itl_company WHERE company_name = "盛全物业"),"(select id from zones where name = '北海公园')", "(select id from zones where name = '北海公园')");
UPDATE zones SET manager_id = (SELECT id FROM user WHERE account = "BHGY0726") WHERE name = "北海公园";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "BHGY0726"), "后台项目管理员");
INSERT INTO itl_zone_category(gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name) VALUES (now(), now(), (SELECT id FROM zones WHERE name = "北海公园"), 11, "项目部");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "CDZC0726", "f8f51d4586102d656e5bdca1a4922686", "时代·长岛之春-管理员", "时代·长岛之春-管理员", (SELECT id FROM itl_company WHERE company_name = "泰杰物业"),"(select id from zones where name = '时代·长岛之春')", "(select id from zones where name = '时代·长岛之春')");
UPDATE zones SET manager_id = (SELECT id FROM user WHERE account = "CDZC0726") WHERE name = "时代·长岛之春";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "CDZC0726"), "后台项目管理员");
INSERT INTO itl_zone_category(gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name) VALUES (now(), now(), (SELECT id FROM zones WHERE name = "时代·长岛之春"), 11, "项目部");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "ZSYT0726", "4895cbf55e841b7c4f0683d351a91346", "中山御庭-管理员", "中山御庭-管理员", (SELECT id FROM itl_company WHERE company_name = "泰杰物业"),"(select id from zones where name = '中山御庭')", "(select id from zones where name = '中山御庭')");
UPDATE zones SET manager_id = (SELECT id FROM user WHERE account = "ZSYT0726") WHERE name = "中山御庭";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "ZSYT0726"), "后台项目管理员");
INSERT INTO itl_zone_category(gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name) VALUES (now(), now(), (SELECT id FROM zones WHERE name = "中山御庭"), 11, "项目部");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "DYGC0726", "7941c40503f453f2c2649f35dd890092", "东园高层公寓-管理员", "东园高层公寓-管理员", (SELECT id FROM itl_company WHERE company_name = "泰杰物业"),"(select id from zones where name = '东园高层公寓')", "(select id from zones where name = '东园高层公寓')");
UPDATE zones SET manager_id = (SELECT id FROM user WHERE account = "DYGC0726") WHERE name = "东园高层公寓";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "DYGC0726"), "后台项目管理员");
INSERT INTO itl_zone_category(gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name) VALUES (now(), now(), (SELECT id FROM zones WHERE name = "东园高层公寓"), 11, "项目部");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "EQDS0726", "4e8b02dbfb0647b22e584656a317516c", "浙江二轻大厦-管理员", "浙江二轻大厦-管理员", (SELECT id FROM itl_company WHERE company_name = "华隆物业"),"(select id from zones where name = '浙江二轻大厦')", "(select id from zones where name = '浙江二轻大厦')");
UPDATE zones SET manager_id = (SELECT id FROM user WHERE account = "EQDS0726") WHERE name = "浙江二轻大厦";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "EQDS0726"), "后台项目管理员");
INSERT INTO itl_zone_category(gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name) VALUES (now(), now(), (SELECT id FROM zones WHERE name = "浙江二轻大厦"), 11, "项目部");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "PSDL0726", "3a9e5b38574982a6898bcd024717942b", "浙江皮塑大楼-管理员", "浙江皮塑大楼-管理员", (SELECT id FROM itl_company WHERE company_name = "华隆物业"),"(select id from zones where name = '浙江皮塑大楼')", "(select id from zones where name = '浙江皮塑大楼')");
UPDATE zones SET manager_id = (SELECT id FROM user WHERE account = "PSDL0726") WHERE name = "浙江皮塑大楼";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "PSDL0726"), "后台项目管理员");
INSERT INTO itl_zone_category(gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name) VALUES (now(), now(), (SELECT id FROM zones WHERE name = "浙江皮塑大楼"), 11, "项目部");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "XXTT0726", "ace541ae880eff00ec500165f2ead864", "西溪天堂-管理员", "西溪天堂-管理员", (SELECT id FROM itl_company WHERE company_name = "玺悦物业"),"(select id from zones where name = '西溪天堂')", "(select id from zones where name = '西溪天堂')");
UPDATE zones SET manager_id = (SELECT id FROM user WHERE account = "XXTT0726") WHERE name = "西溪天堂";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "XXTT0726"), "后台项目管理员");
INSERT INTO itl_zone_category(gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name) VALUES (now(), now(), (SELECT id FROM zones WHERE name = "西溪天堂"), 11, "项目部");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "KXYDS0726", "37ed70ceaab2b5c9e595f8251ed9fccc", "凯喜雅大厦-管理员", "凯喜雅大厦-管理员", (SELECT id FROM itl_company WHERE company_name = "凯喜雅物业"),"(select id from zones where name = '凯喜雅大厦')", "(select id from zones where name = '凯喜雅大厦')");
UPDATE zones SET manager_id = (SELECT id FROM user WHERE account = "KXYDS0726") WHERE name = "凯喜雅大厦";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "KXYDS0726"), "后台项目管理员");
INSERT INTO itl_zone_category(gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name) VALUES (now(), now(), (SELECT id FROM zones WHERE name = "凯喜雅大厦"), 11, "项目部");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "HLYY0726", "21fd34b6814e5c8305ec2109f23d1de1", "黄龙雅苑-管理员", "黄龙雅苑-管理员", (SELECT id FROM itl_company WHERE company_name = "泛亚物业"),"(select id from zones where name = '黄龙雅苑')", "(select id from zones where name = '黄龙雅苑')");
UPDATE zones SET manager_id = (SELECT id FROM user WHERE account = "HLYY0726") WHERE name = "黄龙雅苑";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "HLYY0726"), "后台项目管理员");
INSERT INTO itl_zone_category(gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name) VALUES (now(), now(), (SELECT id FROM zones WHERE name = "黄龙雅苑"), 11, "项目部");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "XXJZ0726", "0cb5f316d9290e5a53be05d1038c867c", "西溪金座-管理员", "西溪金座-管理员", (SELECT id FROM itl_company WHERE company_name = "绿宇物业"),"(select id from zones where name = '西溪金座')", "(select id from zones where name = '西溪金座')");
UPDATE zones SET manager_id = (SELECT id FROM user WHERE account = "XXJZ0726") WHERE name = "西溪金座";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "XXJZ0726"), "后台项目管理员");
INSERT INTO itl_zone_category(gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name) VALUES (now(), now(), (SELECT id FROM zones WHERE name = "西溪金座"), 11, "项目部");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "ZYXQ0726", "5ee7b5a93c4d9214506f956347e64f6c", "政苑小区-管理员", "政苑小区-管理员", (SELECT id FROM itl_company WHERE company_name = "绿宇物业"),"(select id from zones where name = '政苑小区')", "(select id from zones where name = '政苑小区')");
UPDATE zones SET manager_id = (SELECT id FROM user WHERE account = "ZYXQ0726") WHERE name = "政苑小区";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "ZYXQ0726"), "后台项目管理员");
INSERT INTO itl_zone_category(gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name) VALUES (now(), now(), (SELECT id FROM zones WHERE name = "政苑小区"), 11, "项目部");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "BJY0726", "af2b0ad952eae89f0a0106b5d43e12dc", "碧景园-管理员", "碧景园-管理员", (SELECT id FROM itl_company WHERE company_name = "绿宇物业"),"(select id from zones where name = '碧景园')", "(select id from zones where name = '碧景园')");
UPDATE zones SET manager_id = (SELECT id FROM user WHERE account = "BJY0726") WHERE name = "碧景园";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "BJY0726"), "后台项目管理员");
INSERT INTO itl_zone_category(gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name) VALUES (now(), now(), (SELECT id FROM zones WHERE name = "碧景园"), 11, "项目部");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "FHJY0726", "5f89b76c534aca183f49121b946c81e1", "京明凤凰家园-管理员", "京明凤凰家园-管理员", (SELECT id FROM itl_company WHERE company_name = "钱塘物业"),"(select id from zones where name = '京明凤凰家园')", "(select id from zones where name = '京明凤凰家园')");
UPDATE zones SET manager_id = (SELECT id FROM user WHERE account = "FHJY0726") WHERE name = "京明凤凰家园";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "FHJY0726"), "后台项目管理员");
INSERT INTO itl_zone_category(gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name) VALUES (now(), now(), (SELECT id FROM zones WHERE name = "京明凤凰家园"), 11, "项目部");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "HKGY0726", "5095111881eb07e61d0d69a95ad67703", "华克公寓-管理员", "华克公寓-管理员", (SELECT id FROM itl_company WHERE company_name = "钱塘物业"),"(select id from zones where name = '华克公寓')", "(select id from zones where name = '华克公寓')");
UPDATE zones SET manager_id = (SELECT id FROM user WHERE account = "HKGY0726") WHERE name = "华克公寓";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "HKGY0726"), "后台项目管理员");
INSERT INTO itl_zone_category(gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name) VALUES (now(), now(), (SELECT id FROM zones WHERE name = "华克公寓"), 11, "项目部");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "JYYY0726", "2d58e6345778d6f123294763d27cfaf8", "金逸雅苑-管理员", "金逸雅苑-管理员", (SELECT id FROM itl_company WHERE company_name = "钱塘物业"),"(select id from zones where name = '金逸雅苑')", "(select id from zones where name = '金逸雅苑')");
UPDATE zones SET manager_id = (SELECT id FROM user WHERE account = "JYYY0726") WHERE name = "金逸雅苑";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "JYYY0726"), "后台项目管理员");
INSERT INTO itl_zone_category(gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name) VALUES (now(), now(), (SELECT id FROM zones WHERE name = "金逸雅苑"), 11, "项目部");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "MJY0726", "e12dd32473fea728b86d129adda61864", "美郡苑-管理员", "美郡苑-管理员", (SELECT id FROM itl_company WHERE company_name = "钱塘物业"),"(select id from zones where name = '美郡苑')", "(select id from zones where name = '美郡苑')");
UPDATE zones SET manager_id = (SELECT id FROM user WHERE account = "MJY0726") WHERE name = "美郡苑";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "MJY0726"), "后台项目管理员");
INSERT INTO itl_zone_category(gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name) VALUES (now(), now(), (SELECT id FROM zones WHERE name = "美郡苑"), 11, "项目部");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "YDW0726", "5545bc2568e161956ff452eee60fba11", "御东湾-管理员", "御东湾-管理员", (SELECT id FROM itl_company WHERE company_name = "钱塘物业"),"(select id from zones where name = '御东湾')", "(select id from zones where name = '御东湾')");
UPDATE zones SET manager_id = (SELECT id FROM user WHERE account = "YDW0726") WHERE name = "御东湾";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "YDW0726"), "后台项目管理员");
INSERT INTO itl_zone_category(gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name) VALUES (now(), now(), (SELECT id FROM zones WHERE name = "御东湾"), 11, "项目部");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "FCC0726", "a44b9f61b43631a04f181b6ab1259e51", "翡翠城-管理员", "翡翠城-管理员", (SELECT id FROM itl_company WHERE company_name = "测试物业"),"(select id from zones where name = '翡翠城')", "(select id from zones where name = '翡翠城')");
UPDATE zones SET manager_id = (SELECT id FROM user WHERE account = "FCC0726") WHERE name = "翡翠城";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "FCC0726"), "后台项目管理员");
INSERT INTO itl_zone_category(gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name) VALUES (now(), now(), (SELECT id FROM zones WHERE name = "翡翠城"), 11, "项目部");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "YC0726", "edd716d0f00574fd83903feb705d290f", "华盛达阅城-管理员", "华盛达阅城-管理员", (SELECT id FROM itl_company WHERE company_name = "体验物业"),"(select id from zones where name = '华盛达阅城')", "(select id from zones where name = '华盛达阅城')");
UPDATE zones SET manager_id = (SELECT id FROM user WHERE account = "YC0726") WHERE name = "华盛达阅城";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "YC0726"), "后台项目管理员");
INSERT INTO itl_zone_category(gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name) VALUES (now(), now(), (SELECT id FROM zones WHERE name = "华盛达阅城"), 11, "项目部");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "TLCF0726", "9d0bb4e4658c0e068456dfdc185ee323", "桃李春风-管理员", "桃李春风-管理员", (SELECT id FROM itl_company WHERE company_name = "体验物业"),"(select id from zones where name = '桃李春风')", "(select id from zones where name = '桃李春风')");
UPDATE zones SET manager_id = (SELECT id FROM user WHERE account = "TLCF0726") WHERE name = "桃李春风";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "TLCF0726"), "后台项目管理员");
INSERT INTO itl_zone_category(gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name) VALUES (now(), now(), (SELECT id FROM zones WHERE name = "桃李春风"), 11, "项目部");
INSERT INTO user(gmt_create, gmt_modify, account, password, name, nickname, company_id, zone_id, zone_ids) VALUES (now(), now(), "LZRYXQ0726", "6dc2ecfff38f4cd924be7a7e12e80f0b", "离职人员库（虚拟小区）-管理员", "离职人员库（虚拟小区）-管理员", (SELECT id FROM itl_company WHERE company_name = "离职人员"),"(select id from zones where name = '离职人员库（虚拟小区）')", "(select id from zones where name = '离职人员库（虚拟小区）')");
UPDATE zones SET manager_id = (SELECT id FROM user WHERE account = "LZRYXQ0726") WHERE name = "离职人员库（虚拟小区）";
INSERT INTO user_role_relation(gmt_create, gmt_modify, user_id, role_code) VALUES (now(), now(), (SELECT id FROM user WHERE account = "LZRYXQ0726"), "后台项目管理员");
INSERT INTO itl_zone_category(gmt_create, gmt_modify, zone_id, category_pool_id, category_pool_name) VALUES (now(), now(), (SELECT id FROM zones WHERE name = "离职人员库（虚拟小区）"), 11, "项目部");
COMMIT;

# 管家端工具TAB的小区功能隐藏
DROP TABLE IF EXISTS `itl_zone_menu_filter`;
CREATE TABLE `itl_zone_menu_filter` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '数据库自增ID',
  `gmt_create` datetime NOT NULL DEFAULT '1970-01-01 00:00:01' COMMENT '数据创建时间',
  `gmt_modify` datetime NOT NULL DEFAULT '1970-01-01 00:00:01' COMMENT '数据修改时间',
  `zone_id` int(11) NOT NULL COMMENT '小区ID',
  `menu_group_ids` varchar(512) NOT NULL COMMENT '入口分组ID组成的字符串，英文逗号隔开',
  `menu_ids` varchar(512) NOT NULL COMMENT '冗余字段，方便查询，入口ID组成的字符串，英文逗号隔开',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_zone` (`zone_id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COMMENT='小区的入口过滤配置表';

-- ----------------------------
--  Records of `itl_zone_menu_filter`
-- ----------------------------
BEGIN;
INSERT INTO `itl_zone_menu_filter` VALUES ('1', '2017-05-06 18:14:44', '2017-05-06 18:14:44', '1', '18,17,16,15,14,13', '1,2,3,6,7,9,10,12,15,23,27,4,5,8,13,22,11,14,24,25,26,28'), ('2', '2017-05-06 18:14:44', '2017-05-06 18:14:44', '2', '18,17,16,15,14,13', '1,2,3,6,7,9,10,12,15,23,27,4,5,8,13,22,11,14,24,25,26'), ('3', '2017-05-06 18:14:44', '2017-05-06 18:14:44', '5', '3', '1,2,3,6,7,9,10,12,15,23,26,27'), ('4', '2017-05-06 18:14:44', '2017-05-06 18:14:44', '9', '17,15,14,13', '1,2,3,6,7,9,10,12,15,23,27,4,5,8,13,22,26'), ('5', '2017-05-06 18:14:44', '2017-05-06 18:14:44', '10', '17,15,14,13', '1,2,3,6,7,9,10,12,15,23,26,27'), ('6', '2017-05-06 18:14:44', '2017-05-06 18:14:44', '11', '13', '1,2,3,6,7,9,10,12,15,23,26,27'), ('7', '2017-05-06 18:14:44', '2017-05-06 18:14:44', '12', '13', '1,2,3,6,7,9,10,12,15,23,26,27'), ('8', '2017-05-06 18:14:44', '2017-05-06 18:14:44', '13', '13', '1,2,3,6,7,9,10,12,15,23,26,27'), ('9', '2017-05-06 18:14:44', '2017-05-06 18:14:44', '14', '13', '1,2,3,6,7,9,10,12,15,23,26,27'), ('10', '2017-05-06 18:14:45', '2017-05-06 18:14:45', '15', '13', '1,2,3,6,7,9,10,12,15,23,26,27'), ('11', '2017-05-06 18:14:45', '2017-05-06 18:14:45', '16', '13', '1,2,3,6,7,9,10,12,15,23,26,27'), ('12', '2017-05-06 18:14:45', '2017-05-06 18:14:45', '17', '13', '1,2,3,6,7,9,10,12,15,23,26,27'), ('13', '2017-05-06 18:14:45', '2017-05-06 18:14:45', '18', '13', '1,2,3,6,7,9,10,12,15,23,26,27'), ('14', '2017-05-06 18:14:45', '2017-05-06 18:14:45', '19', '13', '1,2,3,6,7,9,10,12,15,23,26,27'), ('15', '2017-05-06 18:14:45', '2017-05-06 18:14:45', '20', '18,17,16,15,14,13', '1,2,3,6,7,9,10,12,15,23,27,4,5,8,13,22,11,14,24,25,26'), ('16', '2017-05-06 18:14:45', '2017-05-06 18:14:45', '21', '15,14,13', '1,2,3,6,7,9,10,12,15,23,26,27'), ('17', '2017-05-06 18:14:45', '2017-05-06 18:14:45', '22', '15,14,13,3', '1,2,3,6,7,9,10,12,15,23,26,27'), ('18', '2017-05-06 18:14:45', '2017-05-06 18:14:45', '23', '15,14,13,3', '1,2,3,6,7,9,10,12,15,23,26,27'), ('19', '2017-05-21 22:04:55', '2017-05-21 22:04:55', '24', '17,15,14,13', '1,2,3,6,7,9,10,12,15,23,26,27,4,5,8,13,22'), ('20', '2017-05-21 22:04:55', '2017-05-21 22:04:55', '25', '17,16,15,14,13', '1,2,3,6,7,9,10,12,15,23,26,27,4,5,8,13,22'), ('21', '2017-05-21 22:04:55', '2017-05-21 22:04:55', '26', '17,16,15,14,13', '1,2,3,6,7,9,10,12,15,23,26,27,4,5,8,13,22'), ('22', '2017-05-21 22:04:55', '2017-05-21 22:04:55', '27', '17,16,15,14,13', '1,2,3,6,7,9,10,12,15,23,26,27,4,5,8,13,22'), ('23', '2017-06-07 00:00:00', '2017-06-07 00:00:00', '28', '15,14,13', '1,2,3,6,7,9,10,12,15,23,26,27'), ('25', '1970-01-01 00:00:01', '2017-07-10 00:00:00', '29', '15,14,13', '1,2,3,6,7,9,10,12,15,23,26,27'), ('26', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '30', '15,14,13', '1,2,3,6,7,9,10,12,15,23,26,27'), ('27', '2017-07-18 07:50:29', '2017-07-18 07:50:29', '31', '13,8,7,6', '2619,2599,2597,2734,2735,2736,2737,2738,2739,2740,2741,2742,2743,2745,2746,2753,2756,2757,2758,2759,2760,2761,2762,2763,2764,2765,2766,2767,2768,2769,2770,2771'), ('28', '2017-07-18 09:17:16', '2017-07-18 09:17:16', '33', '15,14,13,8,7,6', '2619,2599,2597,2734,2735,2736,2737,2738,2739,2740,2741,2742,2743,2745,2746,2753,2756,2757,2758,2759,2760,2761,2762,2763,2764,2765,2766,2767,2768,2769,2770,2771'), ('29', '2017-07-18 09:25:12', '2017-07-18 09:25:12', '32', '15,14,13,8,7,6', '2619,2599,2597,2734,2735,2736,2737,2738,2739,2740,2741,2742,2743,2745,2746,2753,2756,2757,2758,2759,2760,2761,2762,2763,2764,2765,2766,2767,2768,2769,2770,2771'), ('30', '2017-07-19 21:01:52', '2017-07-19 21:01:52', '34', '16,17,18,6,7,8,9,10,11,13,14,15', '2734,2735,2736,2737,2738,2739,2740,2741,2742,2743,2745,2746,2753,2756,2757,2758,2759,2760,2761,2762,2763,2764,2765,2766,2767,2768,2769,2770,2771,2754,2755,2747,2748,2749,2744,2750,2752,2751'), ('31', '2017-07-21 14:26:11', '2017-07-21 14:26:11', '35', '18,17,16,15,14,13,11,10,9,8,7,6', ''), ('32', '2017-07-25 19:30:03', '2017-07-25 19:30:03', '36', '6,9,14', ''), ('33', '2017-07-26 10:35:33', '2017-07-26 10:35:33', '37', '6,13', ''), ('34', '2017-07-26 10:41:02', '2017-07-26 10:41:02', '38', '19,6,7,8,9,13,14,15', '');
COMMIT;

# 老小区的临时任务处理
