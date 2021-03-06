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
SET `id` = '9', `zone_id` = '2', `module` = '17', `name` = '小区收支', `url` = 'http://preuser.itianluo.cn/shouzhigongkai?targetUrl=http://preuser.itianluo.cn/money?1=1&firstLoad=1',
  `icon` = 'http://itianluo-apiupload.oss-cn-hangzhou.aliyuncs.com/itl/test/p/c8befafd-64df-4c2b-87c1-cb5b3fc97712.png', `status` = '0', `sort_by` = '6'
WHERE (`id` = '9');
UPDATE `itianluo`.`zone_module`
SET `id` = '63', `zone_id` = '1', `module` = '17', `name` = '收支公开', `url` = 'http://preuser.itianluo.cn/shouzhigongkai?targetUrl=http://preuser.itianluo.cn/money?1=1&firstLoad=1',
  `icon` = 'http://itianluo-apiupload.oss-cn-hangzhou.aliyuncs.com/itl/test/p/c8befafd-64df-4c2b-87c1-cb5b3fc97712.png', `status` = '1', `sort_by` = '8'
WHERE (`id` = '63');
UPDATE `itianluo`.`zone_module`
SET `id` = '130', `zone_id` = '34', `module` = '17', `name` = '收支公开',
  `url`  = 'http://preuser.itianluo.cn/shouzhigongkai?targetUrl=http://preuser.itianluo.cn/money?1=1&firstLoad=1',
  `icon` = 'http://itianluo-apiupload.oss-cn-hangzhou.aliyuncs.com/itl/test/p/c8befafd-64df-4c2b-87c1-cb5b3fc97712.png', `status` = '1', `sort_by` = '5'
WHERE (`id` = '130');
UPDATE `itianluo`.`zone_module`
SET `id` = '157', `zone_id` = '76', `module` = '17', `name` = '小区收支',
  `url`  = 'http://preuser.itianluo.cn/shouzhigongkai?targetUrl=http://preuser.itianluo.cn/money?1=1&firstLoad=1',
  `icon` = 'http://itianluo-apiupload.oss-cn-hangzhou.aliyuncs.com/itl/test/p/c8befafd-64df-4c2b-87c1-cb5b3fc97712.png', `status` = '0', `sort_by` = '6'
WHERE (`id` = '157');
UPDATE `itianluo`.`zone_module`
SET `id` = '189', `zone_id` = '2', `module` = '17', `name` = '小区收支', `url` = 'http://preuser.itianluo.cn/shouzhigongkai?targetUrl=http://preuser.itianluo.cn/money?1=1&firstLoad=1',
  `icon` = 'http://itianluo-apiupload.oss-cn-hangzhou.aliyuncs.com/itl/test/p/c8befafd-64df-4c2b-87c1-cb5b3fc97712.png', `status` = '1', `sort_by` = '6'
WHERE (`id` = '189');
UPDATE `itianluo`.`zone_module`
SET `id` = '200', `zone_id` = '76', `module` = '17', `name` = '小区收支',
  `url`  = 'http://preuser.itianluo.cn/shouzhigongkai?targetUrl=http://preuser.itianluo.cn/money?1=1&firstLoad=1',
  `icon` = 'http://itianluo-apiupload.oss-cn-hangzhou.aliyuncs.com/itl/test/p/c8befafd-64df-4c2b-87c1-cb5b3fc97712.png', `status` = '1', `sort_by` = '6'
WHERE (`id` = '200');
UPDATE `itianluo`.`zone_module`
SET `id` = '132', `zone_id` = '34', `module` = '18', `name` = '小区文件', `url` = 'http://preapi.itianluo.cn/html?id=119',
  `icon` = 'http://itianluo-apiupload.oss-cn-hangzhou.aliyuncs.com/itl/test/p/318219f1-0640-4dbf-8cbf-287496533e54.png', `status` = '1', `sort_by` = '7'
WHERE (`id` = '132');
UPDATE `itianluo`.`zone_module`
SET `id` = '143', `zone_id` = '24', `module` = '18', `name` = '文件公开', `url` = 'http://preapi.itianluo.cn/html?id=168',
  `icon` = 'http://itianluo-apiupload.oss-cn-hangzhou.aliyuncs.com/itl/test/p/318219f1-0640-4dbf-8cbf-287496533e54.png', `status` = '1', `sort_by` = '8'
WHERE (`id` = '143');
UPDATE `itianluo`.`zone_module`
SET `id` = '38', `zone_id` = '2', `module` = '11', `name` = '申领垃圾袋', `url` = 'http://preapi.itianluo.cn/html?id=9',
  `icon` = 'http://itianluo-apiupload.oss-cn-hangzhou.aliyuncs.com/itl/test/p/635d6539-bf4c-4725-b345-0fa3153d62da.png', `status` = '0', `sort_by` = '10'
WHERE (`id` = '38');
UPDATE `itianluo`.`zone_module`
SET `id` = '164', `zone_id` = '1', `module` = '22', `name` = '数据中心', `url` = 'http://preeye.itianluo.cn/#/login?1=1',
  `icon` = 'http://itianluo.oss-cn-hangzhou.aliyuncs.com/itl/p/99fda028-977f-49e0-9592-fe61dbd7a80a.png', `status` = '1', `sort_by` = '22'
WHERE (`id` = '164');
UPDATE `itianluo`.`zone_module`
SET `id` = '178', `zone_id` = '76', `module` = '22', `name` = '数据中心', `url` = 'http://preeye.itianluo.cn/#/login?1=1',
  `icon` = 'http://itianluo.oss-cn-hangzhou.aliyuncs.com/itl/p/99fda028-977f-49e0-9592-fe61dbd7a80a.png', `status` = '0', `sort_by` = '22'
WHERE (`id` = '178');
UPDATE `itianluo`.`zone_module`
SET `id` = '148', `zone_id` = '1', `module` = '21', `name` = '审批', `url` = 'http://preuser.itianluo.cn/approvallist?1=1',
  `icon` = 'http://itianluo.oss-cn-hangzhou.aliyuncs.com/itl/p/650d4363-f6df-419e-8a76-fbeeaab2b477.png', `status` = '1', `sort_by` = '21'
WHERE (`id` = '148');
UPDATE `itianluo`.`zone_module`
SET `id` = '159', `zone_id` = '76', `module` = '21', `name` = '审批', `url` = 'http://preuser.itianluo.cn/approvallist?1=1',
  `icon` = 'http://itianluo.oss-cn-hangzhou.aliyuncs.com/itl/p/650d4363-f6df-419e-8a76-fbeeaab2b477.png', `status` = '0', `sort_by` = '9'
WHERE (`id` = '159');
UPDATE `itianluo`.`zone_module`
SET `id` = '112', `zone_id` = '24', `module` = '17', `name` = '收支公开', `url` = 'http://preuser.itianluo.cn/html5?id=126',
  `icon` = 'http://itianluenergyo-apiupload.oss-cn-hangzhou.aliyuncs.com/itl/test/p/c8befafd-64df-4c2b-87c1-cb5b3fc97712.png', `status` = '1', `sort_by` = '5'
WHERE (`id` = '112');
UPDATE `itianluo`.`zone_module`
SET `id` = '201', `zone_id` = '76', `module` = '18', `name` = '小区文件', `url` = 'http://preuser.itianluo.cn/html5?id=432',
  `icon` = 'http://itianluo-apiupload.oss-cn-hangzhou.aliyuncs.com/itl/test/p/318219f1-0640-4dbf-8cbf-287496533e54.png', `status` = '0', `sort_by` = '8'
WHERE (`id` = '201');

UPDATE `itianluo`.`itl_parking`
SET `id`       = '2', `created_time` = '2017-10-16 21:24:41', `modified_time` = '2017-11-30 10:52:50', `zone_id` = '1', `name` = '1-02', `group_name` = '1栋',
  `owner_type` = '私家', `house_info_id` = '9906', `contact` = '胡明浩', `contact_mobile` = '15022222222', `can_temp_park` = '0', `is_locked` = '0', `can_rent` = '0',
  `rent_start` = NULL, `rent_end` = NULL, `rent_remark` = '', `can_sell` = '0', `sell_remark` = '', `coordinate` = '742,360;779,315;800,334;764,377', `last_operator` = '1047'
WHERE (`id` = '2');
UPDATE `itianluo`.`itl_parking`
SET `id`       = '3', `created_time` = '2017-10-16 21:24:41', `modified_time` = '2017-11-30 11:00:35', `zone_id` = '1', `name` = '1-03', `group_name` = '1栋',
  `owner_type` = '私家', `house_info_id` = '9906', `contact` = '胡明浩', `contact_mobile` = '15022222222', `can_temp_park` = '0', `is_locked` = '0', `can_rent` = '0',
  `rent_start` = NULL, `rent_end` = NULL, `rent_remark` = '', `can_sell` = '0', `sell_remark` = '', `coordinate` = '707,330;744,286;765,304;728,353', `last_operator` = '1047'
WHERE (`id` = '3');
UPDATE `itianluo`.`itl_parking`
SET `id`       = '4', `created_time` = '2017-10-16 21:24:41', `modified_time` = '2017-11-30 10:57:03', `zone_id` = '1', `name` = '1-04', `group_name` = '1栋',
  `owner_type` = '私家', `house_info_id` = '3140', `contact` = '刘艳青', `contact_mobile` = '13616555604', `can_temp_park` = '0', `is_locked` = '0', `can_rent` = '0',
  `rent_start` = NULL, `rent_end` = NULL, `rent_remark` = '', `can_sell` = '0', `sell_remark` = '', `coordinate` = '685,312;723,267;744,286;707,330', `last_operator` = '1047'
WHERE (`id` = '4');
UPDATE `itianluo`.`itl_parking`
SET `id`       = '5', `created_time` = '2017-10-16 21:24:41', `modified_time` = '2017-11-30 10:57:10', `zone_id` = '1', `name` = '1-05', `group_name` = '1栋',
  `owner_type` = '私家', `house_info_id` = '3140', `contact` = '刘艳青', `contact_mobile` = '13616555604', `can_temp_park` = '0', `is_locked` = '0', `can_rent` = '0',
  `rent_start` = NULL, `rent_end` = NULL, `rent_remark` = '', `can_sell` = '0', `sell_remark` = '', `coordinate` = '663,293;700,250;723,267;685,312', `last_operator` = '1047'
WHERE (`id` = '5');
UPDATE `user`
SET `password` = 'e10adc3949ba59abbe56e057f20f883e';
UPDATE users
SET passwd = 'e10adc3949ba59abbe56e057f20f883e';
UPDATE express_users
SET `password` = 'e10adc3949ba59abbe56e057f20f883e';
UPDATE zones
SET `name` = CONCAT('pre', `name`);

COMMIT;