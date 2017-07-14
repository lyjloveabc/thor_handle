# 所有已经存在的账单给新添加的is_checked、financial_income字段设置默认值
UPDATE bill SET is_checked=1, financial_income=ought_amount;

