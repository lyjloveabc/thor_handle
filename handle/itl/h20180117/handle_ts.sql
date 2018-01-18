BEGIN;
###### START 处理商铺公共维修费 ######
# 删除2017年度的账期
DELETE FROM subscription_period
WHERE zone_id = 76 AND id = 179;

# 更新18年度的账期
UPDATE subscription_period
SET
  last_period_id = NULL,
  period_name    = '商铺公共维修费 2017年12月-2018年11月',
  period_start   = '2017-12-01',
  period_end     = '2018-11-30'
WHERE zone_id = 76 AND id = 180;

# 删除17年度的账单
DELETE FROM bill
WHERE zone_id = 76 AND sub_period_id = 179;

# 更新18年度的账单
UPDATE bill
SET
  title          = '商铺公共维修费 2017年12月-2018年11月',
  billing_period = '商铺公共维修费 2017年12月-2018年11月',
  gmt_start      = '2017-12-01',
  gmt_end        = '2018-11-30'
WHERE zone_id = 76 AND id = 180;

###### START 处理住宅公共维修费 ######
# 删除2017年度的账期
DELETE FROM subscription_period
WHERE zone_id = 76 AND id = 181;

# 删除2019年度以及之后的账期
DELETE FROM subscription_period
WHERE zone_id = 76 AND id IN (183, 184, 185, 186);

# 更新18年度的账期
UPDATE subscription_period
SET
  last_period_id = NULL,
  period_name    = '住宅公共维修费 2017年12月-2018年11月',
  period_start   = '2017-12-01',
  period_end     = '2018-11-30'
WHERE zone_id = 76 AND id = 182;

# 删除17年度的账单
DELETE FROM bill
WHERE zone_id = 76 AND sub_period_id = 181;

# 删除18年度以及之后的账单
DELETE FROM bill
WHERE zone_id = 76 AND sub_period_id IN (183, 184, 185, 186);

# 更新18年度的账单
UPDATE bill
SET
  title          = '住宅公共维修费 2017年12月-2018年11月',
  billing_period = '住宅公共维修费 2017年12月-2018年11月',
  gmt_start      = '2017-12-01',
  gmt_end        = '2018-11-30'
WHERE zone_id = 76 AND id = 182;

COMMIT;