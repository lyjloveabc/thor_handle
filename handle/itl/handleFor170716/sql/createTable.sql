################################ START 审批 ################################
# 20170615 审批发起记录
DROP TABLE IF EXISTS `itl_approval`;
CREATE TABLE `itl_approval` (
  `id`                  INT          NOT NULL  AUTO_INCREMENT
  COMMENT '数据库自增ID',
  `created_time`        DATETIME     NOT NULL  DEFAULT '1970-01-01 00:00:00'
  COMMENT '数据创建时间',
  `modified_time`       DATETIME     NOT NULL  DEFAULT '1970-01-01 00:00:00'
  COMMENT '数据修改时间',

  `code`                VARCHAR(8)   NOT NULL
  COMMENT '审批单号，单个小区唯一，全范围可以重复。格式：',
  `user_id`             INT          NOT NULL
  COMMENT '发起人ID',
  `zone_id`             INT          NOT NULL
  COMMENT '小区ID',
  `company_id`          INT          NOT NULL
  COMMENT '公司ID',
  `current_exe_user_id` INT          NOT NULL
  COMMENT '当前审批者',

  `content`             VARCHAR(256) NOT NULL
  COMMENT '审批内容',
  `images`              VARCHAR(512) NOT NULL  DEFAULT ''
  COMMENT '审批图片的url地址，多张图片用英文逗号隔开',

  `status`              TINYINT      NOT NULL  DEFAULT 1
  COMMENT '审批状态：1审批中、2审批完成',
  `result`              TINYINT      NOT NULL  DEFAULT 0
  COMMENT '审批结果：1审批通过、2审批拒绝',

  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_code_company`(`code`, `company_id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COMMENT '审批发起记录';

# 20170615 审批流记录
DROP TABLE IF EXISTS `itl_approval_flow`;
CREATE TABLE `itl_approval_flow` (
  `id`            INT          NOT NULL  AUTO_INCREMENT
  COMMENT '数据库自增ID',
  `created_time`  DATETIME     NOT NULL  DEFAULT '1970-01-01 00:00:00'
  COMMENT '数据创建时间',
  `modified_time` DATETIME     NOT NULL  DEFAULT '1970-01-01 00:00:00'
  COMMENT '数据修改时间',

  `user_id`       INT          NOT NULL
  COMMENT '审批人ID',
  `approval_id`   INT          NOT NULL
  COMMENT '具体哪一条审批的ID',
  `zone_id`       INT          NOT NULL
  COMMENT '项目ID',
  `company_id`    INT          NOT NULL
  COMMENT '公司ID',

  `content`       VARCHAR(256) NOT NULL
  COMMENT '审批内容',
  `images`        VARCHAR(512) NOT NULL  DEFAULT ''
  COMMENT '审批图片的url地址，多张图片用英文逗号隔开',

  `is_executed`   TINYINT      NOT NULL  DEFAULT 0
  COMMENT '是否已经执行审批：1执行了、0未执行',
  `result`        TINYINT      NOT NULL  DEFAULT 0
  COMMENT '操作结果：1操作通过（同意）、2操作拒绝（拒绝）',

  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COMMENT '审批流记录';
################################ END 审批 ################################

################################ START 考勤 ################################
# 20170518 考勤日志表
DROP TABLE IF EXISTS `itl_attendance_log`;
CREATE TABLE `itl_attendance_log` (
  `id`             INT          NOT NULL  AUTO_INCREMENT
  COMMENT '数据库自增ID',
  `gmt_create`     DATETIME     NOT NULL  DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据创建时间',
  `gmt_modify`     DATETIME     NOT NULL  DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据修改时间',

  `user_id`        INT          NOT NULL
  COMMENT '用户ID',
  `zone_id`        INT          NOT NULL
  COMMENT '小区ID',
  `job_title_id`   INT(11)      NOT NULL  DEFAULT '0'
  COMMENT '头衔ID',
  `job_title_name` VARCHAR(32)  NOT NULL  DEFAULT ''
  COMMENT '头衔名称',
  `image`          VARCHAR(256) NOT NULL  DEFAULT ''
  COMMENT '考勤照片',
  `type`           VARCHAR(512) NOT NULL  DEFAULT '1'
  COMMENT '考勤类型：1上班打卡，0下班打卡',

  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COMMENT '考勤日志表';
################################ END 考勤 ################################

################################ START 咨询 ################################
# 20170523 员工常用语
DROP TABLE IF EXISTS `itl_user_common_phrase`;
CREATE TABLE `itl_user_common_phrase` (
  `id`         INT          NOT NULL  AUTO_INCREMENT
  COMMENT '数据库自增ID',
  `gmt_create` DATETIME     NOT NULL  DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据创建时间',
  `gmt_modify` DATETIME     NOT NULL  DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据修改时间',

  `user_id`    INT          NOT NULL
  COMMENT '用户ID',
  `content`    VARCHAR(256) NOT NULL  DEFAULT ''
  COMMENT '常用语内容',

  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COMMENT '员工常用语';
################################ END 咨询 ################################

################################ START 账单打折记录 ################################
# 201707056 账单打折记录（一条打折账单一条记录）
DROP TABLE IF EXISTS `itl_bill_discount_log`;
CREATE TABLE `itl_bill_discount_log` (
  `id`             INT            NOT NULL          AUTO_INCREMENT
  COMMENT '数据库自增ID',
  `created_time`   DATETIME       NOT NULL          DEFAULT '1970-01-01 00:00:00'
  COMMENT '数据创建时间',
  `modified_time`  DATETIME       NOT NULL          DEFAULT '1970-01-01 00:00:00'
  COMMENT '数据修改时间',

  `user_id`        INT            NOT NULL
  COMMENT '执行打折的人ID',
  `bill_id`        INT            NOT NULL
  COMMENT '账单的ID',
  `zone_id`        INT            NOT NULL
  COMMENT '小区ID',

  `approval_id`    INT                              DEFAULT NULL
  COMMENT '打折的审批id',

  `discount_num`   DECIMAL(10, 2)                   DEFAULT NULL
  COMMENT '折扣数值，实收金额和应收金额的比值',
  `discount_money` DECIMAL(10, 2) NOT NULL          DEFAULT 0
  COMMENT '优惠金额，折扣了多少钱，应收金额减去实收金额',

  `remark`         VARCHAR(128)   NOT NULL
  COMMENT '折扣说明',

  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COMMENT '账单打折记录（一条打折账单一条记录）';
################################ END 账单打折记录 ################################

################################ START 物业上传文件的状态记录 ################################
# 物业上传文件的状态记录
CREATE TABLE `itianluo`.`itl_wuye_file_upload` (
  `id`            INT          NOT NULL,
  `zone_id`       INT          NOT NULL,
  `type`          VARCHAR(45)  NOT NULL
  COMMENT '任务,房屋,业主',
  `file`          VARCHAR(150) NOT NULL,
  `state`         VARCHAR(45)  NOT NULL
  COMMENT '已处理,未处理',
  `modified_time` DATETIME     NULL,
  `created_time`  DATETIME     NULL,
  PRIMARY KEY (`id`)
);

ALTER TABLE `itianluo`.`itl_wuye_file_upload`
  CHANGE COLUMN `id` `id` INT(11) NOT NULL AUTO_INCREMENT;
################################ END 物业上传文件的状态记录 ################################
