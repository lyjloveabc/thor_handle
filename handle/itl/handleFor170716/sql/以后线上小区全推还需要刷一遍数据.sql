# 更新现有小区的公司名称

# 所有的人员更新公司
UPDATE user LEFT JOIN zones ON zones.id = user.zone_id SET user.company_id = zones.company_id;

