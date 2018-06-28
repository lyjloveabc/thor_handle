BEGIN;

# 整改计划表
# 1、整改计划list，按照状态排序：进行中>未开始>已完成>已终止，同状态下按照时间由近到远排序
DROP TABLE IF EXISTS `itl_rectify_plan`;
CREATE TABLE `itl_rectify_plan` (
  `id`                    INT         NOT NULL         AUTO_INCREMENT,
  `gmt_create`            DATETIME    NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据创建时间',
  `gmt_modified`          DATETIME    NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据修改时间',

  `zone_id`               INT         NOT NULL
  COMMENT '小区ID',
  `curr_zone_category_id` INT                          DEFAULT NULL
  COMMENT '发布者当前所在小区部门ID',

  `title`                 VARCHAR(30) NOT NULL
  COMMENT '计划的标题',
  `content`               VARCHAR(300)                 DEFAULT NULL
  COMMENT '计划的内容',
  `images`                VARCHAR(800)                 DEFAULT NULL
  COMMENT '计划的图片',
  `plan_complete_time`    DATE        NOT NULL
  COMMENT '计划完成时间',
  `publisher`             INT         NOT NULL
  COMMENT '发布者ID，物业人员',

  `start_time`            DATETIME                     DEFAULT NULL
  COMMENT '启动时间',
  `start_user_id`         INT                          DEFAULT NULL
  COMMENT '启动人，物业人员',
  `complete_time`         DATETIME                     DEFAULT NULL
  COMMENT '完成时间',
  `complete_user_id`      INT                          DEFAULT NULL
  COMMENT '完成人人，物业人员',
  `stop_time`             DATETIME                     DEFAULT NULL
  COMMENT '中止时间',
  `stop_id`               INT                          DEFAULT NULL
  COMMENT '中止人，物业人员',

  `status`                TINYINT     NOT NULL
  COMMENT '状态：1-进行中、2-未开始、3-已完成、4-已终止',

  `info_adjusted`         TINYINT     NOT NULL         DEFAULT 0
  COMMENT '是否被信息调整了:1-被调整了、0未被调整',
  `task_dispatched`       TINYINT     NOT NULL         DEFAULT 0
  COMMENT '是否派发了任务:1-派发了、0没有派发任务',

  PRIMARY KEY (`id`),
  INDEX `idx_zone`(`zone_id`)
)
  COMMENT = '整改计划表'
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

# 整改计划留言表
DROP TABLE IF EXISTS `itl_rectify_plan_msg`;
CREATE TABLE `itl_rectify_plan_msg` (
  `id`              INT         NOT NULL         AUTO_INCREMENT,
  `gmt_create`      DATETIME    NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据创建时间',
  `gmt_modified`    DATETIME    NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据修改时间',

  `rectify_plan_id` INT         NOT NULL
  COMMENT '整改计划ID',

  `prefix`          VARCHAR(20)                  DEFAULT NULL
  COMMENT '留言前缀',
  `content`         VARCHAR(300)                 DEFAULT NULL
  COMMENT '留言的内容',
  `images`          VARCHAR(800)                 DEFAULT NULL
  COMMENT '留言的图片',

  `operate_type`    VARCHAR(20) NOT NULL
  COMMENT '操作类型不同产生的留言：PUBLISH-发布、ADJUST-信息调整、STOP-中止、START-启动、DISPATCH_TASK-派发任务、FINISHED-确认完成、LEAVE-留言',

  `creator_id`      INT         NOT NULL
  COMMENT '留言者ID，物业人员',

  PRIMARY KEY (`id`),
  INDEX `idx_rectify_plan`(`rectify_plan_id`)
)
  COMMENT = '整改计划留言表'
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

# 整改计划派发任务表
DROP TABLE IF EXISTS `itl_rectify_plan_task`;
CREATE TABLE `itl_rectify_plan_task` (
  `id`               INT      NOT NULL         AUTO_INCREMENT,
  `gmt_create`       DATETIME NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据创建时间',
  `gmt_modified`     DATETIME NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据修改时间',

  `rectify_plan_id`  INT      NOT NULL
  COMMENT '整改计划ID',

  `launch_task_id`   INT      NOT NULL
  COMMENT '发布任务ID',
  `dispatch_user_id` INT      NOT NULL
  COMMENT '派发这ID，物业人员',

  PRIMARY KEY (`id`),
  INDEX `idx_rectify_plan`(`rectify_plan_id`),
  INDEX `idx_launch_task`(`launch_task_id`)
)
  COMMENT = '整改计划派发任务表'
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

# 整改计划信息调整表
DROP TABLE IF EXISTS `itl_rectify_plan_adjust`;
CREATE TABLE `itl_rectify_plan_adjust` (
  `id`                     INT      NOT NULL         AUTO_INCREMENT,
  `gmt_create`             DATETIME NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据创建时间',
  `gmt_modified`           DATETIME NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据修改时间',

  `rectify_plan_id`        INT      NOT NULL
  COMMENT '整改计划ID',

  `old_content`            VARCHAR(300)              DEFAULT NULL
  COMMENT '老的计划的内容',
  `old_images`             VARCHAR(800)              DEFAULT NULL
  COMMENT '老的计划的内容',
  `old_plan_complete_time` DATE                      DEFAULT NULL
  COMMENT '老的计划完成时间',

  `operator_id`            INT      NOT NULL
  COMMENT '操作者',

  PRIMARY KEY (`id`),
  INDEX `idx_rectify_plan`(`rectify_plan_id`)
)
  COMMENT = '整改计划信息调整表'
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

###### START 品质检查 ######
# 品质检查表
DROP TABLE IF EXISTS `itl_quality_check`;
CREATE TABLE `itl_quality_check` (
  `id`                    INT         NOT NULL         AUTO_INCREMENT,
  `gmt_create`            DATETIME    NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据创建时间',
  `gmt_modified`          DATETIME    NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据修改时间',

  `zone_id`               INT         NOT NULL
  COMMENT '小区ID',
  `curr_zone_category_id` INT                          DEFAULT NULL
  COMMENT '发布者当前所在小区部门ID',

  `title`                 VARCHAR(30) NOT NULL
  COMMENT '品检的标题',
  `publisher`             INT         NOT NULL
  COMMENT '发布者ID，物业人员',

  `total_count`           INT         NOT NULL
  COMMENT '检查总数',
  `checked_count`         INT         NOT NULL
  COMMENT '已经检查的数量',
  `qualified_count`       INT         NOT NULL
  COMMENT '合格的数量',

  PRIMARY KEY (`id`),
  INDEX `idx_zone`(`zone_id`)
)
  COMMENT = '品质检查表'
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

# 品检业务数据关联表
DROP TABLE IF EXISTS `itl_quality_check_biz`;
CREATE TABLE `itl_quality_check_biz` (
  `id`               INT         NOT NULL         AUTO_INCREMENT,
  `gmt_create`       DATETIME    NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据创建时间',
  `gmt_modified`     DATETIME    NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据修改时间',

  `quality_check_id` INT         NOT NULL
  COMMENT '品检ID',
  `add_user_id`      INT         NOT NULL
  COMMENT '添加人ID',

  `biz_type`         VARCHAR(20) NOT NULL
  COMMENT '业务类型：REPAIR-报修、POST_THING-报事、COMPLAIN-投诉、PRAISE-表扬、SAMPLING-抽检、TASK-任务',
  `biz_id`           INT         NOT NULL
  COMMENT '业务ID',

  `content`          VARCHAR(300)                 DEFAULT NULL
  COMMENT '品检的内容',
  `images`           VARCHAR(800)                 DEFAULT NULL
  COMMENT '品检的图片',
  `check_result`     TINYINT     NOT NULL
  COMMENT '品检结果：一星=非常差、二星=待改进、三星=合格、四星=较好、五星=非常好',
  `check_user_id`    INT         NOT NULL
  COMMENT '品检的人',

  PRIMARY KEY (`id`),
  INDEX `idx_quality_check`(`quality_check_id`),
  INDEX `idx_biz_type`(`biz_type`),
  INDEX `idx_biz`(`biz_id`)
)
  COMMENT = '品检业务数据关联表'
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

# ------------------ 相关业务表新增品检ID字段，null或0表示未品检，>0表示已品检 ------------------
ALTER TABLE `task`
  ADD `quality_check_biz_id` INT NULL
COMMENT '品检检查的ID';

ALTER TABLE `itl_post_thing_log`
  ADD `quality_check_biz_id` INT NULL
COMMENT '品检检查的ID';

ALTER TABLE `appraisal`
  ADD `quality_check_biz_id` INT NULL
COMMENT '品检检查的ID';

ALTER TABLE `itl_do_task`
  ADD `quality_check_biz_id` INT NULL
COMMENT '品检检查的ID';

###### START 标签管理 ######
# 标签库
DROP TABLE IF EXISTS `itl_label`;
CREATE TABLE `itl_label` (
  `id`           INT          NOT NULL         AUTO_INCREMENT,
  `gmt_create`   DATETIME     NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据创建时间',
  `gmt_modified` DATETIME     NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据修改时间',

  `group_name`   VARCHAR(30)  NOT NULL
  COMMENT '标签组名称',
  `label_name`   VARCHAR(30)  NOT NULL
  COMMENT '标签名称',
  `remark`       VARCHAR(100) NULL
  COMMENT '标签说明、标签备注',

  `stopped`      TINYINT      NOT NULL         DEFAULT 0
  COMMENT '是否停用：1-停用了、0未停用',

  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_gl`(`group_name`, `label_name`),
  INDEX `idx_group_name`(`group_name`)
)
  COMMENT = '标签库'
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

# 打标签
DROP TABLE IF EXISTS `itl_biz_label`;
CREATE TABLE `itl_biz_label` (
  `id`           INT         NOT NULL         AUTO_INCREMENT,
  `gmt_create`   DATETIME    NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据创建时间',
  `gmt_modified` DATETIME    NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据修改时间',

  `biz_type`     VARCHAR(20) NOT NULL
  COMMENT '业务类型：REPAIR-报修、POST_THING-报事、COMPLAIN-投诉、PRAISE-表扬、TASK-任务、TASK_POOL-任务库、KNOWLEDGE-知识库',
  `biz_id`       INT         NOT NULL
  COMMENT '业务ID',

  `label_name`   VARCHAR(30) NOT NULL
  COMMENT '标签名称',

  PRIMARY KEY (`id`),
  INDEX `idx_biz_type`(`biz_type`)
)
  COMMENT = '打标签'
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

###### START 任务check ######
# 任务标准表
DROP TABLE IF EXISTS `itl_task_standard`;
CREATE TABLE `itl_task_standard` (
  `id`           INT          NOT NULL         AUTO_INCREMENT,
  `gmt_create`   DATETIME     NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据创建时间',
  `gmt_modified` DATETIME     NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据修改时间',

  `zone_task_id` INT          NOT NULL
  COMMENT 'itl_zone_task表的ID',
  `standard`     VARCHAR(100) NOT NULL
  COMMENT '标准内容',

  PRIMARY KEY (`id`),
  INDEX `idx_zone_task`(`zone_task_id`)
)
  COMMENT = '任务标准表'
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

# 任务执行任务标准表
DROP TABLE IF EXISTS `itl_do_task_standard`;
CREATE TABLE `itl_do_task_standard` (
  `id`           INT          NOT NULL         AUTO_INCREMENT,
  `gmt_create`   DATETIME     NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据创建时间',
  `gmt_modified` DATETIME     NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据修改时间',

  `do_task_id`   INT          NOT NULL
  COMMENT 'itl_do_task表的ID',
  `standard`     VARCHAR(100) NOT NULL
  COMMENT '标准内容',

  `checked`      TINYINT      NOT NULL         DEFAULT 0
  COMMENT '是否已经勾选：0-未结构选、1-已勾选',

  PRIMARY KEY (`id`),
  INDEX `idx_do_task`(`do_task_id`)
)
  COMMENT = '任务标准表'
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

###### START 知识库 ######
# 知识类型表
DROP TABLE IF EXISTS `itl_knowledge_type`;
CREATE TABLE `itl_knowledge_type` (
  `id`           INT         NOT NULL         AUTO_INCREMENT,
  `gmt_create`   DATETIME    NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据创建时间',
  `gmt_modified` DATETIME    NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据修改时间',

  `name`         VARCHAR(30) NOT NULL
  COMMENT 'itl_do_task表的ID',

  PRIMARY KEY (`id`)
)
  COMMENT = '任务标准表'
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

# 知识库
DROP TABLE IF EXISTS `itl_knowledge_pool`;
CREATE TABLE `itl_knowledge_pool` (
  `id`                INT          NOT NULL         AUTO_INCREMENT,
  `gmt_create`        DATETIME     NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据创建时间',
  `gmt_modified`      DATETIME     NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据修改时间',

  `zone_id`           INT          NOT NULL
  COMMENT '小区ID',

  `knowledge_type_id` INT          NOT NULL
  COMMENT '类型ID',

  `title`             VARCHAR(30)  NOT NULL
  COMMENT '标题',
  `content_url`       VARCHAR(300) NOT NULL
  COMMENT '内容H5跳转超链接',

  `stopped`           TINYINT      NOT NULL         DEFAULT 0
  COMMENT '是否停用：1-停用了、0未停用',

  PRIMARY KEY (`id`),
  INDEX `idx_zone`(`zone_id`),
  INDEX `idx_knowledge_type`(`knowledge_type_id`)
)
  COMMENT = '知识库'
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

# 知识已读
DROP TABLE IF EXISTS `itl_knowledge_read`;
CREATE TABLE `itl_knowledge_pool` (
  `id`                INT      NOT NULL         AUTO_INCREMENT,
  `gmt_create`        DATETIME NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据创建时间',
  `gmt_modified`      DATETIME NOT NULL         DEFAULT '1970-01-01 00:00:01'
  COMMENT '数据修改时间',

  `knowledge_pool_id` INT      NOT NULL
  COMMENT '知识ID',
  `staff_id`          INT      NOT NULL
  COMMENT '管家ID',

  PRIMARY KEY (`id`),
  INDEX `idx_knowledge_pool`(`knowledge_pool_id`),
  INDEX `idx_staff_id`(`staff_id`)
)
  COMMENT = '知识已读'
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

COMMIT;