from utils.constant.constant import Constant

sql = """
SET @u_id = (SELECT id
             FROM `user`
             WHERE account = '{account}');

SET @c_name = (SELECT category_name
               FROM `user`
               WHERE account = '{account}');

UPDATE user
SET
  category_id = (SELECT id
                 FROM itl_zone_category
                 WHERE itl_zone_category.zone_id = {zone_id} AND itl_zone_category.category_pool_name = @c_name
  ),
  zone_id     = {zone_id},
  zone_ids    = {zone_id}
WHERE id = @u_id;

UPDATE itl_user_zone_relation
SET zone_id = {zone_id}
WHERE user_id = @u_id;

DELETE FROM itl_user_task
WHERE user_id = @u_id;
"""

accounts = [
    '18258933399',
    '13736461886',
]

with open('out.sql', 'a') as f:
    f.write(Constant.SQL_BEGIN)
    for account in accounts:
        f.write(sql.format(account=account, zone_id=85))
    f.write(Constant.SQL_COMMIT)
