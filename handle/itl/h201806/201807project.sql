BEGIN;

# 报修的收费标准表
DROP TABLE IF EXISTS `itl_repair_charge`;
CREATE TABLE `itl_repair_charge` (
  `id`           INT          NOT NULL         AUTO_INCREMENT,
  `gmt_create`   DATETIME     NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据创建时间',
  `gmt_modified` DATETIME     NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据修改时间',

  `zone_id`      INT          NOT NULL
  COMMENT '小区ID',
  `content_url`  VARCHAR(200) NOT NULL
  COMMENT '内容H5跳转超链接',

  `operator_id`  INT          NOT NULL
  COMMENT '操作人',

  PRIMARY KEY (`id`),
  INDEX `idx_zone`(`zone_id`)
)
  COMMENT = '报修的收费标准表'
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

# 通知信息流表
DROP TABLE IF EXISTS `itl_hold_notice`;
CREATE TABLE `itl_hold_notice` (
  `id`            INT          NOT NULL         AUTO_INCREMENT,
  `gmt_create`    DATETIME     NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据创建时间',
  `gmt_modified`  DATETIME     NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据修改时间',

  `zone_id`       INT          NOT NULL
  COMMENT '小区ID',
  `house_info_id` INT          NOT NULL
  COMMENT '房号ID',
  `hold_id`       INT          NOT NULL
  COMMENT '住户ID',

  `be_read`       TINYINT      NOT NULL         DEFAULT 0
  COMMENT '是否已读：1-已读、0-未读',

  `biz_type`      VARCHAR(20)  NOT NULL
  COMMENT '业务类型：CA-认证通知、COMPLAIN-投诉、PRAISE-表扬、REPAIR-报修、POST_THING-报事',
  `biz_id`        INT          NOT NULL
  COMMENT '业务数据ID',

  `title`         VARCHAR(50)  NOT NULL
  COMMENT '标题',
  `content`       VARCHAR(200) NOT NULL
  COMMENT '内容',

  PRIMARY KEY (`id`),
  INDEX `idx_zone`(`zone_id`),
  INDEX `idx_hold_id`(`hold_id`),
  INDEX `idx_biz_type`(`biz_type`)
)
  COMMENT = '通知信息流表'
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

COMMIT;