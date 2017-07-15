START TRANSACTION;

# 添加车位费product_type
INSERT INTO product_type (id, name, bill_name, code, icon, gmt_create, gmt_modify, description, status)
VALUES (27, '车位费', '车位费', 'parking', 'producttype/170406/1491477935.png', now(), now(), '', 'VALID');

# 添加车位费product
INSERT INTO product (id, name, product_type_id, product_type_code, period, gmt_create, gmt_modify, fee_rule, status)
VALUES (16, '车位费', 27, 'parking', 'month', now(), now(), '{"type":"common","UnitAmounts":[{"dosage":0,"unitAmount":1.95}],"feeRule":"count * unitPrice"}', 'VALID');

# 所有的部门
INSERT INTO `itl_category_pool` VALUES ('11', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '项目'), ('12', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '客服部'), ('13', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '财务部'), ('15', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '行政内务部'), ('16', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '工程部'), ('17', '1970-01-01 00:00:01', '1970-01-01 00:00:01', '环境部');

COMMIT;