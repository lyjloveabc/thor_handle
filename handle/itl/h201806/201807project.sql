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


COMMIT;