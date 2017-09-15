role_code_str = '客服负责人、管家客服、前台客服、保安负责人、门岗、巡逻岗、车库岗、监控岗、工程负责人、工程、弱电、高配'
role_codes = role_code_str.split('、')

print(role_codes)
for role_code in role_codes:
    print('INSERT INTO role_permission_relation(gmt_create, gmt_modify, role_code, permission_code) VALUES (now(), now(), "' + role_code + '", "housekeeper_emergency");')
