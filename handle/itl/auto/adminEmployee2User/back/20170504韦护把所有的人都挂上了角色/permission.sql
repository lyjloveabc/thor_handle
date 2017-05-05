/*
 Navicat MySQL Data Transfer

 Source Server         : dev
 Source Server Version : 50542
 Source Host           : 192.168.1.101
 Source Database       : itianluo

 Target Server Version : 50542
 File Encoding         : utf-8

 Date: 05/04/2017 20:20:03 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `permission`
-- ----------------------------
DROP TABLE IF EXISTS `permission`;
CREATE TABLE `permission` (
  `id` int(32) NOT NULL AUTO_INCREMENT COMMENT '数据库自增ID',
  `gmt_create` datetime NOT NULL DEFAULT '1970-01-01 00:00:01' COMMENT '数据创建时间',
  `gmt_modify` datetime NOT NULL DEFAULT '1970-01-01 00:00:01' COMMENT '数据修改时间',
  `parent_id` int(32) NOT NULL DEFAULT '0' COMMENT '父级权限',
  `code` varchar(128) NOT NULL COMMENT '权限编码',
  `name` varchar(128) NOT NULL COMMENT '权限名称',
  `type` varchar(32) NOT NULL COMMENT '权限类型: FUNCTION功能权限, MENU菜单权限，COMMONLY_TOOL常用工具（用于首页）',
  `function_url` varchar(512) NOT NULL DEFAULT '' COMMENT '功能路径',
  `menu_type` varchar(16) NOT NULL DEFAULT '' COMMENT '菜单类型',
  `icon_url` varchar(256) NOT NULL DEFAULT '' COMMENT 'icon路径',
  `description` varchar(256) NOT NULL DEFAULT '' COMMENT '权限描述',
  `sort_num` mediumint(9) NOT NULL DEFAULT '1' COMMENT '排序字段',
  `checked` varchar(8) NOT NULL DEFAULT 'TRUE' COMMENT '是否默认选择: TRUE是, FALSE不选中',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_code_type` (`code`,`type`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COMMENT='权限表 permission';

-- ----------------------------
--  Records of `permission`
-- ----------------------------
BEGIN;
INSERT INTO `permission` VALUES ('1', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '0', 'attendanceRecords', '考勤记录', 'MENU', '', '1', 'http://oda3qkbe9.bkt.clouddn.com/icon-kaoqin@3x.png', '新管家“工具”的菜单：考勤记录', '1', 'TRUE'), ('2', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '0', 'myTask', '我的任务', 'MENU', '', '2', 'http://oda3qkbe9.bkt.clouddn.com/icon-gangweirenwu@3x.png', '新管家“工具”的菜单：我的任务', '2', 'TRUE'), ('3', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '0', 'distributedTask', '派发任务', 'MENU', '', '3', 'http://oda3qkbe9.bkt.clouddn.com/icon-paifa@3x.png', '新管家“工具”的菜单：派发任务', '3', 'TRUE'), ('4', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '0', 'complaints', '投诉', 'MENU', '', '4', 'http://oda3qkbe9.bkt.clouddn.com/icon-tousu@3x.png', '新管家“工具”的菜单：投诉', '4', 'TRUE'), ('5', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '0', 'praise', '表扬', 'MENU', '', '5', 'http://oda3qkbe9.bkt.clouddn.com/icon-biaoyang@3x.png', '新管家“工具”的菜单：表扬', '5', 'TRUE'), ('6', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '0', 'repairServiceDispatching', '报修派工', 'MENU', '', '6', 'http://oda3qkbe9.bkt.clouddn.com/icon-baoxiu@3x.png', '新管家“工具”的菜单：报修派工', '6', 'TRUE'), ('7', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '0', 'repairMaintenance', '报修维修', 'MENU', '', '7', 'http://oda3qkbe9.bkt.clouddn.com/icon-baoxiu@3x.png', '新管家“工具”的菜单：报修维修', '7', 'TRUE'), ('8', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '0', 'inAndOutManagement', '出入管理', 'MENU', '', '8', 'http://oda3qkbe9.bkt.clouddn.com/icon-churu@3x.png', '新管家“工具”的菜单：出入管理', '8', 'TRUE'), ('9', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '0', 'draftBox', '草稿箱', 'MENU', '', '9', 'http://oda3qkbe9.bkt.clouddn.com/icon-caogao@3x.png', '新管家“工具”的菜单：草稿箱', '9', 'TRUE'), ('10', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '0', 'summaryPlan', '总结计划', 'MENU', '', '10', 'http://oda3qkbe9.bkt.clouddn.com/icon-zongjie@3x.png', '新管家“工具”的菜单：总结计划', '10', 'TRUE'), ('11', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '0', 'communityExpress', '小区快递', 'MENU', '', '11', 'http://oda3qkbe9.bkt.clouddn.com/icon-kuaidi@3x.png', '新管家“工具”的菜单：小区快递', '11', 'TRUE'), ('12', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '0', 'employeeSituation', '员工信息', 'MENU', '', '12', 'http://oda3qkbe9.bkt.clouddn.com/icon-yuangong@3x.png', '新管家“工具”的菜单：员工信息', '12', 'TRUE'), ('13', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '0', 'householdSituation', '住户信息', 'MENU', '', '13', 'http://oda3qkbe9.bkt.clouddn.com/icon-zhuhu@3x.png', '新管家“工具”的菜单：住户信息', '13', 'TRUE'), ('14', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '0', 'energyMeterReading', '能耗抄表', 'MENU', '', '14', 'http://oda3qkbe9.bkt.clouddn.com/icon-nenghao@3x.png', '新管家“工具”的菜单：能耗抄表', '14', 'TRUE'), ('15', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '0', 'bonusPoints', '加分扣分', 'MENU', '', '15', 'http://oda3qkbe9.bkt.clouddn.com/icon-jiafen@3x.png', '新管家“工具”的菜单：加分扣分', '15', 'TRUE'), ('19', '2017-02-28 10:19:58', '2017-02-28 10:19:58', '0', 'releaseTask', '发布任务', 'COMMONLY_TOOL', '', '1', '', '新管家“首页”右上角加号：发布任务', '1', 'TRUE'), ('20', '2017-02-28 10:19:58', '2017-02-28 10:19:58', '0', 'releaseMatter', '发布报事', 'COMMONLY_TOOL', '', '2', '', '新管家“首页”右上角加号：发布任务', '2', 'TRUE'), ('21', '2017-02-28 10:19:58', '2017-02-28 10:19:58', '0', 'releaseRepair', '发布报修', 'COMMONLY_TOOL', '', '3', '', '新管家“首页”右上角加号：发布任务', '3', 'TRUE'), ('22', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '0', 'consulting', '咨询', 'MENU', '', '16', 'http://oda3qkbe9.bkt.clouddn.com/icon-zixun@3x.png', '咨询', '16', 'TRUE'), ('23', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '0', 'postAdjustment', '岗位调整', 'MENU', '', '17', 'http://oda3qkbe9.bkt.clouddn.com/icon-gangweitiaozheng@3x.png', '岗位调整', '17', 'TRUE'), ('24', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '0', 'propertyCharge', '物业收费', 'MENU', '', '18', 'http://oda3qkbe9.bkt.clouddn.com/icon-wuyeshoufei@3x.png', '物业收费', '18', 'TRUE'), ('25', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '0', 'otherCharge', '其他收费', 'MENU', '', '19', 'http://oda3qkbe9.bkt.clouddn.com/icon-qitashoufei@3x.png', '其他收费', '19', 'TRUE'), ('26', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '0', 'dataCenter', '数据中心', 'MENU', 'http://eye.itianluo.cn/#/login', '10001', 'http://oda3qkbe9.bkt.clouddn.com/icon-shuju@3x.png', '数据中心', '20', 'TRUE'), ('27', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '0', 'patrol', '巡更', 'MENU', '', '20', 'http://oda3qkbe9.bkt.clouddn.com/icon-xungeng@3x.png', '巡更', '21', 'TRUE'), ('28', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '0', 'taskSampling', '任务抽检', 'MENU', '', '21', 'http://oda3qkbe9.bkt.clouddn.com/icon-choujian@3x.png', '任务抽检', '22', 'TRUE');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
