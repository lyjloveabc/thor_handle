BEGIN;

# 20171127 设备主体表
DROP TABLE IF EXISTS `itl_equipment`;
CREATE TABLE `itl_equipment` (
  `id`                INT          NOT NULL AUTO_INCREMENT
  COMMENT '数据库自增ID',
  `created_time`      DATETIME     NOT NULL DEFAULT '1970-01-01 00:00:00'
  COMMENT '数据创建时间',
  `modified_time`     DATETIME     NOT NULL DEFAULT '1970-01-01 00:00:00'
  COMMENT '数据修改时间',

  `zone_id`           INT          NOT NULL
  COMMENT '小区ID',

  `code`              VARCHAR(32)  NOT NULL
  COMMENT '设备编码，全局唯一',
  `type`              VARCHAR(6)   NOT NULL
  COMMENT '设备类型，枚举值在项目中。目前：1-其他、2-电梯、3-给水、4-排水、5-消防、6-人防、7-强电、8-弱点、9-泳池',
  `name`              VARCHAR(32)  NOT NULL
  COMMENT '设备名',
  `model`             VARCHAR(32)  NULL
  COMMENT '型号',
  `factory`           VARCHAR(32)  NULL
  COMMENT '厂家',
  `factory_code`      VARCHAR(32)  NULL
  COMMENT '设备出厂编号',
  `production_date`   DATE         NULL
  COMMENT '出厂日期，格式：年-月-日',
  `use_date`          DATE         NULL
  COMMENT '使用日期，格式：年-月-日',
  `service_life`      SMALLINT     NULL
  COMMENT '使用期限，单位：年',
  `self_param`        VARCHAR(128) NULL
  COMMENT '自定义参数',
  `other_description` VARCHAR(128) NULL
  COMMENT '其他说明',

  `status`            VARCHAR(8)   NOT NULL DEFAULT 'NORMAL'
  COMMENT '设备状态：NORMAL-正常、ABNORMAL-异常、TROUBLE-故障、SCRAP-报废',
  `beLost`            TINYINT      NOT NULL DEFAULT 0
  COMMENT '是否丢失：1丢失、0未丢',
  `level`             CHAR(1)      NOT NULL DEFAULT 'A'
  COMMENT '设备评级：A、B、C、D、E',
  `install_location`  VARCHAR(32)  NOT NULL
  COMMENT '安装位置',

  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_code` (`code`),
  INDEX `idx_type`(`type`),
  INDEX `idx_name`(`name`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COMMENT '设备主体表';

# 20171127 设备保养标准
DROP TABLE IF EXISTS `itl_equipment_maintain_standard`;
CREATE TABLE `itl_equipment_maintain_standard` (
  `id`               INT          NOT NULL AUTO_INCREMENT
  COMMENT '数据库自增ID',
  `created_time`     DATETIME     NOT NULL DEFAULT '1970-01-01 00:00:00'
  COMMENT '数据创建时间',
  `modified_time`    DATETIME     NOT NULL DEFAULT '1970-01-01 00:00:00'
  COMMENT '数据修改时间',

  `equipment_type`   VARCHAR(6)   NOT NULL
  COMMENT '设备类型，枚举值在项目中。目前：1-其他、2-电梯、3-给水、4-排水、5-消防、6-人防、7-强电、8-弱点、9-泳池',
  `equipment_name`   VARCHAR(32)  NOT NULL
  COMMENT '设备名',

  `standard_content` VARCHAR(128) NOT NULL
  COMMENT '保养标准内容',

  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_type_name` (`equipment_type`, `equipment_name`),
  INDEX `idx_name`(`equipment_name`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COMMENT '设备保养标准';

# 20171120 预算或支出人员流转
DROP TABLE IF EXISTS `itl_budget_approval_flow`;
CREATE TABLE `itl_budget_approval_flow` (
  `id`                 INT(11)      NOT NULL AUTO_INCREMENT
  COMMENT '数据库自增ID',
  `created_time`       DATETIME     NOT NULL DEFAULT '1970-01-01 00:00:00'
  COMMENT '数据创建时间',
  `modified_time`      DATETIME     NOT NULL DEFAULT '1970-01-01 00:00:00'
  COMMENT '数据修改时间',

  `group_value`        INT          NOT NULL
  COMMENT '流转组值',
  `budget_approval_id` INT          NOT NULL
  COMMENT '预算或支出审批主体的ID',

  `exe_id`             INT          NOT NULL
  COMMENT '操作这个审批同意拒绝的人的ID，业主/物业人员的userId',
  `exe_type`           VARCHAR(6)   NOT NULL
  COMMENT '操作者类型，枚举值：STAFF、OWNER',

  `reason`             VARCHAR(128) NULL
  COMMENT '理由',
  `images`             VARCHAR(512) NULL
  COMMENT '图片的url地址，多张图片用英文逗号隔开',
  `is_executed`        TINYINT(4)   NOT NULL DEFAULT '0'
  COMMENT '是否已经执行审批：1执行了、0未执行',
  `result`             TINYINT(4)   NULL
  COMMENT '操作结果：1操作通过（同意）、2操作拒绝（拒绝）',

  PRIMARY KEY (`id`),
  UNIQUE KEY `uk` (`group_value`, `budget_approval_id`, `exe_id`),
  INDEX `idx`(`budget_approval_id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COMMENT '预算或支出人员流转';

#################################### START 初始化数据 ####################################


COMMIT;