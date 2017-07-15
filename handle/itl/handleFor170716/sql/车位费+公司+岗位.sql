START TRANSACTION;

# 添加车位费product_type
INSERT INTO product_type (id, name, bill_name, code, icon, gmt_create, gmt_modify, description, status)
VALUES (27, '车位费', '车位费', 'parking', 'producttype/170406/1491477935.png', now(), now(), '', 'VALID');

# 添加车位费product
INSERT INTO product (id, name, product_type_id, product_type_code, period, gmt_create, gmt_modify, fee_rule, status)
VALUES (16, '车位费', 27, 'parking', 'month', now(), now(), '{"type":"common","UnitAmounts":[{"dosage":0,"unitAmount":1.95}],"feeRule":"count * unitPrice"}', 'VALID');

# 添加目前的全部的公司
INSERT INTO itl_company(id, company_name, status, comment, created_time, modified_time, modified_by, alias) VALUES ("1", "公明物业", "1", "公明物业", now(), now(), "0", "公明物业");
INSERT INTO itl_company(id, company_name, status, comment, created_time, modified_time, modified_by, alias) VALUES ("2", "万源城业委会", "1", "万源城业委会", now(), now(), "0", "万源城业委会");
INSERT INTO itl_company(id, company_name, status, comment, created_time, modified_time, modified_by, alias) VALUES ("3", "盛全物业", "1", "盛全物业", now(), now(), "0", "盛全物业");
INSERT INTO itl_company(id, company_name, status, comment, created_time, modified_time, modified_by, alias) VALUES ("4", "泰杰物业", "1", "泰杰物业", now(), now(), "0", "泰杰物业");
INSERT INTO itl_company(id, company_name, status, comment, created_time, modified_time, modified_by, alias) VALUES ("5", "华隆物业", "1", "华隆物业", now(), now(), "0", "华隆物业");
INSERT INTO itl_company(id, company_name, status, comment, created_time, modified_time, modified_by, alias) VALUES ("6", "玺悦物业", "1", "玺悦物业", now(), now(), "0", "玺悦物业");
INSERT INTO itl_company(id, company_name, status, comment, created_time, modified_time, modified_by, alias) VALUES ("7", "凯喜雅物业", "1", "凯喜雅物业", now(), now(), "0", "凯喜雅物业");
INSERT INTO itl_company(id, company_name, status, comment, created_time, modified_time, modified_by, alias) VALUES ("8", "泛亚物业", "1", "泛亚物业", now(), now(), "0", "泛亚物业");
INSERT INTO itl_company(id, company_name, status, comment, created_time, modified_time, modified_by, alias) VALUES ("9", "绿宇物业", "1", "绿宇物业", now(), now(), "0", "绿宇物业");
INSERT INTO itl_company(id, company_name, status, comment, created_time, modified_time, modified_by, alias) VALUES ("10", "钱塘物业", "1", "钱塘物业", now(), now(), "0", "钱塘物业");
INSERT INTO itl_company(id, company_name, status, comment, created_time, modified_time, modified_by, alias) VALUES ("11", "测试物业", "1", "测试物业", now(), now(), "0", "测试物业");
INSERT INTO itl_company(id, company_name, status, comment, created_time, modified_time, modified_by, alias) VALUES ("12", "体验物业", "1", "体验物业", now(), now(), "0", "体验物业");
INSERT INTO itl_company(id, company_name, status, comment, created_time, modified_time, modified_by, alias) VALUES ("13", "离职人员", "1", "离职人员", now(), now(), "0", "离职人员");

# 更新现有小区的公司名称
UPDATE zones SET company_id = "11" WHERE id = "1";
UPDATE zones SET company_id = "1" WHERE id = "2";
UPDATE zones SET company_id = "13" WHERE id = "5";
UPDATE zones SET company_id = "9" WHERE id = "9";
UPDATE zones SET company_id = "8" WHERE id = "10";
UPDATE zones SET company_id = "12" WHERE id = "11";
UPDATE zones SET company_id = "12" WHERE id = "12";
UPDATE zones SET company_id = "10" WHERE id = "13";
UPDATE zones SET company_id = "10" WHERE id = "14";
UPDATE zones SET company_id = "10" WHERE id = "15";
UPDATE zones SET company_id = "10" WHERE id = "16";
UPDATE zones SET company_id = "10" WHERE id = "17";
UPDATE zones SET company_id = "6" WHERE id = "18";
UPDATE zones SET company_id = "9" WHERE id = "19";
UPDATE zones SET company_id = "12" WHERE id = "20";
UPDATE zones SET company_id = "3" WHERE id = "21";
UPDATE zones SET company_id = "3" WHERE id = "22";
UPDATE zones SET company_id = "7" WHERE id = "23";
UPDATE zones SET company_id = "2" WHERE id = "24";
UPDATE zones SET company_id = "4" WHERE id = "25";
UPDATE zones SET company_id = "4" WHERE id = "26";
UPDATE zones SET company_id = "4" WHERE id = "27";
UPDATE zones SET company_id = "5" WHERE id = "28";
UPDATE zones SET company_id = "9" WHERE id = "29";
UPDATE zones SET company_id = "5" WHERE id = "30";

# 所有的人员更新公司
UPDATE user LEFT JOIN zones ON zones.id = user.zone_id SET user.company_id = zones.company_id;

# 添加所有的岗位
INSERT INTO itl_job_title (id, gmt_create, gmt_modify, name, duties, remark, type) VALUES ('1', now(), now(), '项目负责人', '', '项目总经理、项目经理、管理处主任', '项目');
INSERT INTO itl_job_title (id, gmt_create, gmt_modify, name, duties, remark, type) VALUES ('2', now(), now(), '项目副职', '', '项目副总、项目副经理、项目经理助理', '项目');
INSERT INTO itl_job_title (id, gmt_create, gmt_modify, name, duties, remark, type) VALUES ('3', now(), now(), '客服负责人', '', '项目客服总监、客服经理、客服主管、客服主任', '项目');
INSERT INTO itl_job_title (id, gmt_create, gmt_modify, name, duties, remark, type) VALUES ('4', now(), now(), '客服', '', '管家、楼宇管家、前台客服、楼宇客服、综合管理员、综合客服', '项目');
INSERT INTO itl_job_title (id, gmt_create, gmt_modify, name, duties, remark, type) VALUES ('5', now(), now(), '财务人员', '', '收费员、二级财务、综管员', '项目');
INSERT INTO itl_job_title (id, gmt_create, gmt_modify, name, duties, remark, type) VALUES ('6', now(), now(), '行政内务', '', '综合管理员、综管员、行政专员、行政人事、综合内务', '项目');
INSERT INTO itl_job_title (id, gmt_create, gmt_modify, name, duties, remark, type) VALUES ('7', now(), now(), '工程负责人', '', '项目工程总监、工程经理、工程主管、工程主任', '项目');
INSERT INTO itl_job_title (id, gmt_create, gmt_modify, name, duties, remark, type) VALUES ('8', now(), now(), '工程', '', '水电工、维修工、工程技术员', '项目');
INSERT INTO itl_job_title (id, gmt_create, gmt_modify, name, duties, remark, type) VALUES ('9', now(), now(), '高配工', '', '高压配电工、高压值班员', '项目');
INSERT INTO itl_job_title (id, gmt_create, gmt_modify, name, duties, remark, type) VALUES ('10', now(), now(), '弱电工', '', '弱电工程员、弱电技术员', '项目');
INSERT INTO itl_job_title (id, gmt_create, gmt_modify, name, duties, remark, type) VALUES ('11', now(), now(), '保安负责人', '', '项目保安总监、保安经理、保安主管、保安主任、保安队长', '项目');
INSERT INTO itl_job_title (id, gmt_create, gmt_modify, name, duties, remark, type) VALUES ('12', now(), now(), '保安领班', '', '保安班长', '项目');
INSERT INTO itl_job_title (id, gmt_create, gmt_modify, name, duties, remark, type) VALUES ('13', now(), now(), '保安', '', '秩序维护员、安全管理员、护卫队员', '项目');
INSERT INTO itl_job_title (id, gmt_create, gmt_modify, name, duties, remark, type) VALUES ('14', now(), now(), '环境负责人', '', '环境经理、环境主管、环境主任、环境领班', '项目');
INSERT INTO itl_job_title (id, gmt_create, gmt_modify, name, duties, remark, type) VALUES ('15', now(), now(), '保洁负责人', '', '保洁经理、保洁主管、保洁主任', '项目');
INSERT INTO itl_job_title (id, gmt_create, gmt_modify, name, duties, remark, type) VALUES ('16', now(), now(), '保洁员', '', '清洁工、卫生员、晶面技工', '项目');
INSERT INTO itl_job_title (id, gmt_create, gmt_modify, name, duties, remark, type) VALUES ('17', now(), now(), '绿化负责人', '', '绿化经理、绿化主管、绿化主任、绿化领班', '项目');
INSERT INTO itl_job_title (id, gmt_create, gmt_modify, name, duties, remark, type) VALUES ('18', now(), now(), '绿化工', '', '绿化技工', '项目');

COMMIT;