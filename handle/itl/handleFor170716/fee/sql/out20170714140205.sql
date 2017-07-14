# 添加车位费product_type
INSERT INTO product_type (id, name, bill_name, code, icon, gmt_create, gmt_modify, description, status)VALUES(27, '车位费', '车位费', 'parking', 'producttype/170406/1491477935.png', now(), now(), '', 'VALID');

# 添加车位费product
INSERT INTO product (id, name, product_type_id, product_type_code, period, gmt_create, gmt_modify,fee_rule, status)VALUES(16, '车位费', 27, 'parking', 'month', now(), now(), '{"type":"common","UnitAmounts":[{"dosage":0,"unitAmount":1.95}],"feeRule":"count * unitPrice"}', 'VALID');

