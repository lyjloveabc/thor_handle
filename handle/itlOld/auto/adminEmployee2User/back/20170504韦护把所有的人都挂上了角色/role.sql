/*
 Navicat MySQL Data Transfer

 Source Server         : dev
 Source Server Version : 50542
 Source Host           : 192.168.1.101
 Source Database       : itianluo

 Target Server Version : 50542
 File Encoding         : utf-8

 Date: 05/04/2017 20:20:55 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `role`
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
  `id` int(32) NOT NULL AUTO_INCREMENT COMMENT '数据库自增ID',
  `gmt_create` datetime NOT NULL DEFAULT '1970-01-01 00:00:01' COMMENT '数据创建时间',
  `gmt_modify` datetime NOT NULL DEFAULT '1970-01-01 00:00:01' COMMENT '数据修改时间',
  `code` varchar(128) NOT NULL COMMENT '角色编码',
  `name` varchar(128) NOT NULL COMMENT '角色名称',
  `description` varchar(256) NOT NULL COMMENT '角色描述',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COMMENT='角色表 role';

-- ----------------------------
--  Records of `role`
-- ----------------------------
BEGIN;
INSERT INTO `role` VALUES ('1', '1970-01-01 00:00:01', '1970-01-01 00:00:01', 'fristPermissionSystemAdmin', '第一权限管理员', '拥有账户/权限体系的所有操作权限'), ('2', '1970-01-01 00:00:01', '1970-01-01 00:00:01', 'projectManager', '项目经理', '项目经理'), ('3', '1970-01-01 00:00:01', '1970-01-01 00:00:01', 'customerServiceManager', '客服主管', '客服主管'), ('4', '1970-01-01 00:00:01', '1970-01-01 00:00:01', 'customerServicer', '客服', '客服'), ('5', '1970-01-01 00:00:01', '1970-01-01 00:00:01', 'cleanerManager', '保洁主管', '保洁主管'), ('6', '1970-01-01 00:00:01', '1970-01-01 00:00:01', 'cleaner', '普通保洁', '普通保洁'), ('7', '1970-01-01 00:00:01', '1970-01-01 00:00:01', 'gardener', '绿化工', '绿化工'), ('8', '1970-01-01 00:00:01', '1970-01-01 00:00:01', 'securityManager', '保安队长', '保安队长'), ('9', '1970-01-01 00:00:01', '1970-01-01 00:00:01', 'gateSentry', '门岗形象岗', '门岗形象岗'), ('10', '1970-01-01 00:00:01', '1970-01-01 00:00:01', 'patrolPost', '巡逻岗', '巡逻岗'), ('11', '1970-01-01 00:00:01', '1970-01-01 00:00:01', 'monitoringPost', '监控岗', '监控岗'), ('12', '1970-01-01 00:00:01', '1970-01-01 00:00:01', 'carportSecurity', '车库岗', '车库岗'), ('13', '1970-01-01 00:00:01', '1970-01-01 00:00:01', 'engineeringManager', '工程主管', '工程主管'), ('14', '1970-01-01 00:00:01', '1970-01-01 00:00:01', 'maintainer', '维修工', '维修工'), ('15', '1970-01-01 00:00:01', '1970-01-01 00:00:01', 'outsideMaintainer', '外部维修商', '外部维修商'), ('16', '1970-01-01 00:00:01', '1970-01-01 00:00:01', 'liftWorker', '电梯工', '电梯工'), ('17', '1970-01-01 00:00:01', '1970-01-01 00:00:01', 'energyMeterReader', '能耗抄表员', '能耗抄表员'), ('18', '1970-01-01 00:00:01', '1970-01-01 00:00:01', 'subFinance', '二级财务', '二级财务'), ('19', '1970-01-01 00:00:01', '1970-01-01 00:00:01', 'companyManager', '公司管理层', '公司管理层'), ('20', '1970-01-01 00:00:01', '1970-01-01 00:00:01', 'schrodinger', '外围观测者', '外围观测者'), ('21', '1970-01-01 00:00:01', '1970-01-01 00:00:01', 'toAppStore', '苹果审核专用', '苹果审核专用'), ('22', '1970-01-01 00:00:01', '1970-01-01 00:00:01', 'jobAdjustment', '岗位调整专用', '岗位调整专用');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
