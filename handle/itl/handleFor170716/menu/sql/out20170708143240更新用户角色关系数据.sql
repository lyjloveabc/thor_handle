# 
BEGIN;
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
COMMIT;

# 
BEGIN;
DELETE FROM user_role_relation WHERE role_code IN ('jobAdjustment', 'companyManager', 'energyMeterReader', 'businessExecutive', 'liftWorker');
COMMIT;

# 
BEGIN;
COMMIT;

