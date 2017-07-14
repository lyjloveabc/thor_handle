BEGIN;
insert into user(gmt_create, gmt_modify, account, password, name, identity_card, nickname,sex, mobile, avatar_url, address, email, emergency_contact,emergency_mobile, last_login_time, last_login_ip, category_id,category_name, company_id, zone_id, zone_ids, is_on_job, departure_time,job_title_id, job_title_name, old_user_id) values (now(), now(), "15168220542", "5a015a1fbbfc4b1fb8c1859e03fa6fe8", "邱鸿鑫", "", "邱鸿鑫","M", "15168220542", "", "", "", "","", "1970-01-01 00:00:01", "127.0.0.1", "156","服务中心", "59", 21, "21", "1", "1970-01-01 00:00:01","0", "07/14/2017 11:10:39", "990");
COMMIT;
