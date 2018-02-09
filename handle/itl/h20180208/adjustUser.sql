BEGIN;

####################################
####################################
SET @u_id = (SELECT id
             FROM `user`
             WHERE account = '18367297072');

SET @c_name = (SELECT category_name
               FROM `user`
               WHERE account = '18367297072');

UPDATE user
SET
  category_id = (SELECT id
                 FROM itl_zone_category
                 WHERE itl_zone_category.zone_id = 42 AND itl_zone_category.category_pool_name = @c_name
  ),
  zone_id     = 42,
  zone_ids    = 42
WHERE id = @u_id;

UPDATE itl_user_zone_relation
SET zone_id = 42
WHERE user_id = @u_id;

DELETE FROM itl_user_task
WHERE user_id = @u_id;


COMMIT;
