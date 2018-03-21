BEGIN;

UPDATE `itianluo`.`users`
SET `id`        = '4364', `name` = '胡明浩', `nick` = '飞虎', `nick_opt` = '1', `passwd` = 'e10adc3949ba59abbe56e057f20f883e', `avtar` = '', `sex` = '1', `mobile` = '15011111111',
  `email`       = 'guest@caijia.cn', `create_at` = '1482301829', `update_at` = '1507945116', `type` = '2', `hoster` = '', `relationship` = '', `zone_id` = '1', `house_id` = '5562',
  `house_code`  = '1010101', `address` = '翡翠城南瓜苑1幢1单元0101室', `manager_name` = '管理员', `manager_time` = '1482301858', `ca_image` = '', `ca_status` = '2', `verification_code` = '',
  `device_type` = '1', `device` = '', `version` = '1.3.6', `installationId` = '', `job` = '', `tag` = '', `signature` = '', `identity` = '0', `ghost` = '0'
WHERE (`id` = '4364');
UPDATE `itianluo`.`users`
SET `id`      = '4365', `name` = '胡明浩', `nick` = '小', `nick_opt` = '1', `passwd` = 'e10adc3949ba59abbe56e057f20f883e',
  `avtar`     = 'avtar/2017/10/14/d3e0f226df6865b28fb677548370f467.jpg?v=1507968201', `sex` = '1', `mobile` = '15022222222', `email` = 'guest@caijia.cn',
  `create_at` = '1482302734', `update_at` = '1511747827', `type` = '2', `hoster` = '', `relationship` = '', `zone_id` = '1', `house_id` = '9906', `house_code` = '5010401',
  `address`   = '翡翠城南瓜苑1幢1单元0101室', `manager_name` = '管理员', `manager_time` = '1482302787', `ca_image` = '', `ca_status` = '2', `verification_code` = '', `device_type` = '1',
  `device`    = '', `version` = '1.4.2', `installationId` = '', `job` = 'USB', `tag` = '', `signature` = 'KTV', `identity` = '0', `ghost` = '0', `is_owners_committee` = '1'
WHERE (`id` = '4365');
INSERT INTO `itianluo`.`user_role_relation` (`gmt_create`, `gmt_modify`, `user_id`, `role_code`) VALUES ('2017-11-21 12:03:13', '2017-11-21 12:03:13', '1780', '天眼人员');
UPDATE `itianluo`.`house_info`
SET `id`            = '9906', `code` = '5010401', `zone_id` = '1', `block_id` = '4', `house` = '5', `building` = '1', `door` = '0401', `area` = '80.73', `rooms` = '',
  `decoration`      = '0', `charge` = '0.00', `property_month` = '0.00', `property_fee` = '0.00', `cars_fee` = '0.00', `energy` = '0.00', `water_fee` = '0.00',
  `electricity_fee` = '0.00', `carriage_fee` = '0.00', `parkingspaces` = '1', `status` = '0', `uid` = '4365', `uname` = '施继峰', `mobile` = '15757185534', `notice` = '0',
  `home_at`         = '0', `commercial_kind` = '住宅', `house_floor_num` = '4', `house_kind` = '已入住'
WHERE (`id` = '9906');
UPDATE `itianluo`.`permission`
SET `id`        = '2739', `gmt_create` = '2017-07-10 15:23:05', `gmt_modify` = '2017-07-10 15:23:05', `parent_id` = '0', `code` = 'housekeeper_dataCenter', `name` = '数据中心',
  `type`        = 'MENU', `function_url` = 'http://preeye.itianluo.cn/#/login', `menu_type` = '10001', `icon_url` = 'http://oda3qkbe9.bkt.clouddn.com/icon-shuju@3x.png',
  `description` = '数据中心', `sort_num` = '1000', `checked` = 'TRUE', `menu_kind` = 'WCS_TOOL_TAB'
WHERE (`id` = '2739');
UPDATE `itianluo`.`permission`
SET `id`     = '2763', `gmt_create` = '2017-07-10 15:23:05', `gmt_modify` = '2017-07-10 15:23:05', `parent_id` = '0', `code` = 'HOUSEKEEPER_MY_TAB_我发布的审批', `name` = '我发起的审批',
  `type`     = 'MENU', `function_url` = 'http://preguanjia.itianluo.cn/approvallist?1=1', `menu_type` = '7',
  `icon_url` = 'http://oda3qkbe9.bkt.clouddn.com/icon-faqishenpi@3x.png', `description` = '我发起的审批', `sort_num` = '970', `checked` = 'TRUE', `menu_kind` = 'WCS_MY_TAB'
WHERE (`id` = '2763');
UPDATE `itianluo`.`permission`
SET `id`      = '2813', `gmt_create` = '2017-11-29 10:06:34', `gmt_modify` = '2017-11-29 10:06:34', `parent_id` = '0', `code` = 'housekeeper_expenseApproval', `name` = '支出审批',
  `type`      = 'MENU', `function_url` = 'http://preguanjia.itianluo.cn/expendsubmit?1=1', `menu_type` = '10002',
  `icon_url`  = 'http://itianluo.oss-cn-hangzhou.aliyuncs.com/itl/p/f38ac238-1c7c-49a7-9e91-c5c84269e66f.png', `description` = '支出审批', `sort_num` = '975', `checked` = 'TRUE',
  `menu_kind` = 'WCS_TOOL_TAB'
WHERE (`id` = '2813');
UPDATE `itianluo`.`zone_module`
SET `id` = '9', `zone_id` = '2', `module` = '17', `name` = '收支公开', `url` = 'http://preuser.itianluo.cn/money?1=1&firstLoad=1',
  `icon` = 'http://oda3qkbe9.bkt.clouddn.com/homePage-money.png', `status` = '1', `sort_by` = '8'
WHERE (`id` = '9');
UPDATE `itianluo`.`zone_module`
SET `id` = '38', `zone_id` = '2', `module` = '11', `name` = '申领垃圾袋', `url` = 'http://preapi.itianluo.cn/html?id=9',
  `icon` = 'http://7xn7ft.com2.z0.glb.qiniucdn.com/icon_laji.png', `status` = '0', `sort_by` = '10'
WHERE (`id` = '38');
UPDATE `itianluo`.`zone_module`
SET `id` = '63', `zone_id` = '1', `module` = '17', `name` = '收支公开', `url` = 'http://preuser.itianluo.cn/money?1=1&firstLoad=1',
  `icon` = 'http://oda3qkbe9.bkt.clouddn.com/homePage-money.png', `status` = '1', `sort_by` = '8'
WHERE (`id` = '63');
UPDATE `itianluo`.`zone_module`
SET `id` = '112', `zone_id` = '24', `module` = '17', `name` = '收支公开', `url` = 'http://preapi.itianluo.cn/html?id=126',
  `icon` = 'http://oda3qkbe9.bkt.clouddn.com/homePage-money.png', `status` = '1', `sort_by` = '5'
WHERE (`id` = '112');
UPDATE `itianluo`.`zone_module`
SET `id` = '130', `zone_id` = '34', `module` = '17', `name` = '收支公开', `url` = 'http://preapi.itianluo.cn/html?id=126',
  `icon` = 'http://oda3qkbe9.bkt.clouddn.com/homePage-money.png', `status` = '1', `sort_by` = '5'
WHERE (`id` = '130');
UPDATE `itianluo`.`zone_module`
SET `id` = '132', `zone_id` = '34', `module` = '18', `name` = '小区文件', `url` = 'http://preapi.itianluo.cn/html?id=119',
  `icon` = 'http://itianluo.oss-cn-hangzhou.aliyuncs.com/images/xiaoquwenjian.jpg', `status` = '1', `sort_by` = '7'
WHERE (`id` = '132');
UPDATE `itianluo`.`zone_module`
SET `id` = '143', `zone_id` = '24', `module` = '18', `name` = '文件公开', `url` = 'http://preapi.itianluo.cn/html?id=168',
  `icon` = 'http://itianluo.oss-cn-hangzhou.aliyuncs.com/images/zonefile20170816_yangren.png', `status` = '1', `sort_by` = '8'
WHERE (`id` = '143');
UPDATE `itianluo`.`zone_module`
SET `id` = '148', `zone_id` = '1', `module` = '21', `name` = '审批', `url` = 'http://preuser.itianluo.cn/approvallist?1=1',
  `icon` = 'http://itianluo.oss-cn-hangzhou.aliyuncs.com/images/zone_module_icon/shenpi.png', `status` = '1', `sort_by` = '21'
WHERE (`id` = '148');
UPDATE `user`
SET `password` = 'e10adc3949ba59abbe56e057f20f883e';
UPDATE users
SET passwd = 'e10adc3949ba59abbe56e057f20f883e';


UPDATE permission
SET function_url = 'http://preeye.itianluo.cn/#/login'
WHERE id = 2739;

COMMIT;