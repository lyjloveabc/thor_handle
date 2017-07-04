CREATE TABLE `permission` (
  `id` int(32) NOT NULL AUTO_INCREMENT COMMENT '数据库自增ID',
  `gmt_create` datetime NOT NULL DEFAULT '1970-01-01 00:00:01' COMMENT '数据创建时间',
  `gmt_modify` datetime NOT NULL DEFAULT '1970-01-01 00:00:01' COMMENT '数据修改时间',
  `parent_id` int(32) NOT NULL DEFAULT '0' COMMENT '父级权限',
  `code` varchar(128) NOT NULL COMMENT '权限编码',
  `name` varchar(128) NOT NULL COMMENT '权限名称',
  `type` varchar(32) NOT NULL COMMENT '权限类型: FUNCTION功能权限, MENU菜单权限，COMMONLY_TOOL常用工具（用于首页）',
  `function_url` varchar(512) NOT NULL DEFAULT '' COMMENT '功能路径',
  `menu_type` varchar(16) NOT NULL DEFAULT '' COMMENT '菜单类型，客户端跳转类型',
  `icon_url` varchar(256) NOT NULL DEFAULT '' COMMENT 'icon路径',
  `description` varchar(256) NOT NULL DEFAULT '' COMMENT '权限描述',
  `sort_num` mediumint(9) NOT NULL DEFAULT '1' COMMENT '排序字段',
  `checked` varchar(8) NOT NULL DEFAULT 'TRUE' COMMENT '是否默认选择: TRUE是, FALSE不选中',
  `menu_kind` varchar(32) NOT NULL DEFAULT '' COMMENT '菜单种类',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_code_type` (`code`,`type`)
) ENGINE=InnoDB AUTO_INCREMENT=2677 DEFAULT CHARSET=utf8mb4 COMMENT='权限表 permission'