BEGIN;
insert into user(gmt_create, gmt_modify, account, password, name, identity_card, nickname,sex, mobile, avatar_url, address, email, emergency_contact,emergency_mobile, last_login_time, last_login_ip, category_id,category_name, company_id, zone_id, zone_ids, is_on_job, departure_time,job_title_id, job_title_name, old_user_id) values (now(), now(), "15088794899", "ecb846d2d4bb8238c49370c0ac80a173", "时相配", "", "时相配","M", "15088794899", "", "", "", "","", "1970-01-01 00:00:01", "127.0.0.1", "13","工程维修", "22", 2, "2", "1", "1970-01-01 00:00:01","0", "晚班工程岗", "787");
COMMIT;
