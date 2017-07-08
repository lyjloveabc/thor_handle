# 创建管家端右上角+号的菜单
BEGIN;
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'commonTool_releaseTask', '发布任务', 'MENU', '','1', '', '发布任务', '5', 'TRUE', 'COMMONLY_TOOL');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'commonTool_releaseMatter', '发布报事', 'MENU', '','2', '', '发布报事', '3', 'TRUE', 'COMMONLY_TOOL');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'commonTool_releaseRepair', '发布报修', 'MENU', '','3', '', '发布报修', '4', 'TRUE', 'COMMONLY_TOOL');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'commonTool_markComplaint', '记录投诉', 'MENU', '','4', '', '记录投诉', '2', 'TRUE', 'COMMONLY_TOOL');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'commonTool_markPraise', '记录表扬', 'MENU', '','5', '', '记录表扬', '1', 'TRUE', 'COMMONLY_TOOL');
COMMIT;

# 创建管家端工具入口
BEGIN;
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'housekeeper_dataCenter', '数据中心', 'MENU', 'http://eye.itianluo.cn/#/login','10001', 'http://oda3qkbe9.bkt.clouddn.com/icon-shuju@3x.png', '数据中心', '1000', 'TRUE', 'HOUSEKEEPER');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'housekeeper_repair', '报修', 'MENU', '','1', 'http://oda3qkbe9.bkt.clouddn.com/icon-baoxiu@3x.png', '报修', '999', 'TRUE', 'HOUSEKEEPER');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'housekeeper_postThing', '报事', 'MENU', '','2', 'http://oda3qkbe9.bkt.clouddn.com/icon-baoshi@3x.png', '报事', '998', 'TRUE', 'HOUSEKEEPER');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'housekeeper_complaint', '投诉', 'MENU', '','3', 'http://oda3qkbe9.bkt.clouddn.com/icon-tousu@3x.png', '投诉', '997', 'TRUE', 'HOUSEKEEPER');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'housekeeper_praise', '表扬', 'MENU', '','4', 'http://oda3qkbe9.bkt.clouddn.com/icon-biaoyang@3x.png', '表扬', '996', 'TRUE', 'HOUSEKEEPER');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'housekeeper_consulting', '咨询', 'MENU', '','5', 'http://oda3qkbe9.bkt.clouddn.com/icon-zixun@3x.png', '咨询', '995', 'TRUE', 'HOUSEKEEPER');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'housekeeper_transformWork', '倒班', 'MENU', '','6', 'http://oda3qkbe9.bkt.clouddn.com/icon-daoban@3x.png', '倒班', '994', 'TRUE', 'HOUSEKEEPER');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'housekeeper_staffInfo', '员工信息', 'MENU', '','7', 'http://oda3qkbe9.bkt.clouddn.com/icon-yuangong@3x.png', '员工信息', '993', 'TRUE', 'HOUSEKEEPER');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'housekeeper_propertyCharge', '物业收费', 'MENU', '','8', 'http://oda3qkbe9.bkt.clouddn.com/icon-wuyeshoufei@3x.png', '物业收费', '992', 'TRUE', 'HOUSEKEEPER');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'housekeeper_otherCharge', '其他收费', 'MENU', '','9', 'http://oda3qkbe9.bkt.clouddn.com/icon-qitashoufei@3x.png', '其他收费', '991', 'TRUE', 'HOUSEKEEPER');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'housekeeper_energyReading', '能耗抄表', 'MENU', '','10', 'http://oda3qkbe9.bkt.clouddn.com/icon-nenghao@3x.png', '能耗抄表', '990', 'TRUE', 'HOUSEKEEPER');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'housekeeper_accessManage', '出入管理', 'MENU', '','11', 'http://oda3qkbe9.bkt.clouddn.com/icon-churu@3x.png', '出入管理', '989', 'TRUE', 'HOUSEKEEPER');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'housekeeper_express', '快递', 'MENU', '','12', 'http://oda3qkbe9.bkt.clouddn.com/icon-kuaidi@3x.png', '快递', '988', 'TRUE', 'HOUSEKEEPER');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'housekeeper_household', '住户情况', 'MENU', '','13', 'http://oda3qkbe9.bkt.clouddn.com/icon-zhuhu@3x.png', '住户情况', '987', 'TRUE', 'HOUSEKEEPER');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'housekeeper_taskCenter', '任务中心', 'MENU', '','14', 'http://oda3qkbe9.bkt.clouddn.com/icon-linshi@3x.png', '任务中心', '986', 'TRUE', 'HOUSEKEEPER');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'housekeeper_patrolLog', '巡更记录', 'MENU', '','15', 'http://oda3qkbe9.bkt.clouddn.com/icon-xungeng@3x.png', '巡更记录', '985', 'TRUE', 'HOUSEKEEPER');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'housekeeper_samplingLog', '抽检记录', 'MENU', '','16', 'http://oda3qkbe9.bkt.clouddn.com/icon-choujianjilu@3x.png', '抽检记录', '984', 'TRUE', 'HOUSEKEEPER');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'housekeeper_launchApproval', '发起审批', 'MENU', '','17', 'http://oda3qkbe9.bkt.clouddn.com/icon-faqishenpi@3x.png', '发起审批', '983', 'TRUE', 'HOUSEKEEPER');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'housekeeper_bonusPoint', '加分扣分', 'MENU', '','18', 'http://oda3qkbe9.bkt.clouddn.com/icon-jiafen@3x.png', '加分扣分', '982', 'TRUE', 'HOUSEKEEPER');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'housekeeper_summaryPlan', '总结计划', 'MENU', '','19', 'http://oda3qkbe9.bkt.clouddn.com/icon-zongjie@3x.png', '总结计划', '981', 'TRUE', 'HOUSEKEEPER');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'housekeeper_draftBox', '草稿箱', 'MENU', '','20', 'http://oda3qkbe9.bkt.clouddn.com/icon-caogao@3x.png', '草稿箱', '980', 'TRUE', 'HOUSEKEEPER');
COMMIT;

# 创建管家端我的TAB里面的菜单
BEGIN;
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'HOUSEKEEPER_MY_TAB_我发布的任务', '我发布的任务', 'MENU', '','4', 'http://oda3qkbe9.bkt.clouddn.com/icon-paifa@3x.png', '我发布的任务', '1000', 'TRUE', 'HOUSEKEEPER_MY_TAB');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'HOUSEKEEPER_MY_TAB_我发布的报修', '我发布的报修', 'MENU', '','5', 'http://oda3qkbe9.bkt.clouddn.com/icon-baoxiu@3x.png', '我发布的报修', '990', 'TRUE', 'HOUSEKEEPER_MY_TAB');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'HOUSEKEEPER_MY_TAB_我发布的报事', '我发布的报事', 'MENU', '','6', 'http://oda3qkbe9.bkt.clouddn.com/icon-baoshi@3x.png', '我发布的报事', '980', 'TRUE', 'HOUSEKEEPER_MY_TAB');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'HOUSEKEEPER_MY_TAB_我发布的审批', '我发布的审批', 'MENU', '','7', 'http://oda3qkbe9.bkt.clouddn.com/icon-faqishenpi@3x.png', '我发布的审批', '970', 'TRUE', 'HOUSEKEEPER_MY_TAB');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'HOUSEKEEPER_MY_TAB_我的考勤', '我的考勤', 'MENU', '','8', 'http://oda3qkbe9.bkt.clouddn.com/icon-kaoqin@3x.png', '我的考勤', '960', 'TRUE', 'HOUSEKEEPER_MY_TAB');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'HOUSEKEEPER_MY_TAB_待完成任务', '待完成任务', 'MENU', '','9', 'http://oda3qkbe9.bkt.clouddn.com/icon-linshi@3x.png', '待完成任务', '950', 'TRUE', 'HOUSEKEEPER_MY_TAB');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'HOUSEKEEPER_MY_TAB_待我审批', '待我审批', 'MENU', '','10', 'http://oda3qkbe9.bkt.clouddn.com/icon-daiwoshenpi@3x.png', '待我审批', '940', 'TRUE', 'HOUSEKEEPER_MY_TAB');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'HOUSEKEEPER_MY_TAB_收到的投诉', '收到的投诉', 'MENU', '','11', 'http://oda3qkbe9.bkt.clouddn.com/icon-tousu@3x.png', '收到的投诉', '930', 'TRUE', 'HOUSEKEEPER_MY_TAB');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'HOUSEKEEPER_MY_TAB_收到的表扬', '收到的表扬', 'MENU', '','12', 'http://oda3qkbe9.bkt.clouddn.com/icon-biaoyang@3x.png', '收到的表扬', '920', 'TRUE', 'HOUSEKEEPER_MY_TAB');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'HOUSEKEEPER_MY_TAB_更多', '更多', 'MENU', '','1', 'http://oda3qkbe9.bkt.clouddn.com/icon-zongjie@3x.png', '更多', '910', 'TRUE', 'HOUSEKEEPER_MY_TAB');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'HOUSEKEEPER_MY_TAB_负责小区', '负责小区', 'MENU', '','2', 'http://oda3qkbe9.bkt.clouddn.com/icon-zhuhu@3x.png', '负责小区', '900', 'TRUE', 'HOUSEKEEPER_MY_TAB');
INSERT INTO permission (gmt_create, gmt_modify, parent_id, code, name, type, function_url, menu_type, icon_url, description, sort_num, checked, menu_kind) VALUES (now(), now(), '0', 'HOUSEKEEPER_MY_TAB_岗位职责', '岗位职责', 'MENU', '','3', 'http://oda3qkbe9.bkt.clouddn.com/icon-gangweirenwu@3x.png', '岗位职责', '890', 'TRUE', 'HOUSEKEEPER_MY_TAB');
COMMIT;

