START TRANSACTION;

# 20170627 bill 账单折扣相关
ALTER TABLE bill
  ADD `discount_num` DECIMAL(10, 2) DEFAULT NULL
COMMENT '折扣数值，实收金额和应收金额的比值';

ALTER TABLE bill
  ADD `discount_money` DECIMAL(10, 2) NOT NULL DEFAULT 0
COMMENT '优惠金额，折扣了多少钱，应收金额减去实收金额';

ALTER TABLE bill
  ADD `is_checked` TINYINT NOT NULL DEFAULT 0
COMMENT '该账单是否已经被审核（只有被审核了的账单才会推到前端显示）：1已经被审核；0没有被审核';

ALTER TABLE bill
  ADD `financial_income` DECIMAL(10, 2) NOT NULL DEFAULT 0
COMMENT '财务收入，financial_income=ought_amount-discount_money';

# 增加审批字段
ALTER TABLE `bill`
  ADD COLUMN `approval_id` INT NULL
COMMENT '打折的审批id';

ALTER TABLE zones
  ADD `paid_in_order` TINYINT NOT NULL DEFAULT 0
COMMENT '该小区的账单是否顺序付款，1必须顺序付款，0可以任意付款';

# 20170621 itl_sampling_log 表新增launch_task_id自增ID
ALTER TABLE `itl_sampling_log`
  ADD COLUMN `launch_task_id` INT DEFAULT NULL
COMMENT '这条抽检记录对应的是哪条抽检任务';

# 20170621 itl_zone_category 表新增 leader_user_ids 部门负责人
ALTER TABLE `itl_zone_category`
  ADD COLUMN `leader_user_ids` VARCHAR(256) NOT NULL DEFAULT ''
COMMENT '部门负责人ID字符串，多个用英文字段隔开';

# 20170621 itl_patrol_log 表新增launch_task_id自增ID
ALTER TABLE `itl_patrol_log`
  ADD COLUMN `launch_task_id` INT DEFAULT NULL
COMMENT '这条巡更记录对应的是哪条巡更任务';

# 20170625 itl_sampling_log 表新增do_task_id自增ID
ALTER TABLE `itl_sampling_log`
  ADD COLUMN `do_task_id` INT DEFAULT NULL
COMMENT '这条抽检记录对应的是哪条执行记录';

# 20170621 itl_patrol_log 表新增do_task_id自增ID
ALTER TABLE `itl_patrol_log`
  ADD COLUMN `do_task_id` INT DEFAULT NULL
COMMENT '这条巡更记录对应的是哪条巡更任务';

# 给zones添加初始化需要的字段
ALTER TABLE `zones`
  ADD COLUMN `province` VARCHAR(20) DEFAULT NULL
COMMENT '省份'
  AFTER `company_id`,
  ADD COLUMN `info` TEXT DEFAULT NULL
COMMENT 'son存储额外信息，包含鸟瞰图、正门图、其他备注'
  AFTER `province`,
  ADD COLUMN `type` VARCHAR(20) DEFAULT NULL
COMMENT '项目类型，住宅、写字楼、商业体、其他公建'
  AFTER `info`,
  ADD COLUMN `subtype` VARCHAR(20) DEFAULT NULL
COMMENT '住宅类型：高层、小高层、多层、别墅、排屋'
  AFTER `type`;

# 20170712 user 修改字段可以为空
ALTER TABLE user
  CHANGE `old_user_id` `old_user_id` INT(11) DEFAULT NULL
COMMENT '老的admin_employee的ID';

ALTER TABLE user
  CHANGE `verification_code` `verification_code` VARCHAR(10) DEFAULT NULL
COMMENT '密码注册重置验证码';

COMMIT;