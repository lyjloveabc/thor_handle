BEGIN;

UPDATE user
SET
  gmt_modify    = now(),
  category_id   = 575,
  category_name = '项目部',
  zone_id       = 76,
  zone_ids      = 76
WHERE id = 1914;

UPDATE itl_user_zone_relation
SET modified_time = now(), zone_id = 76
WHERE user_id = 1914;

DELETE FROM itl_user_task
WHERE user_id = 1914;

INSERT INTO user_role_relation (gmt_create, gmt_modify, user_id, role_code) VALUES
  (now(), now(), 1914, '天眼人员'),
  (now(), now(), 454, '天眼人员');

COMMIT;