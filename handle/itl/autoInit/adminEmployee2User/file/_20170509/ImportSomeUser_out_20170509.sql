BEGIN;
insert into user(gmt_create, gmt_modify, account, password, name, identity_card, nickname,sex, mobile, avatar_url, address, email, emergency_contact,emergency_mobile, last_login_time, last_login_ip, category_id,category_name, company_id, zone_id, zone_ids, is_on_job, departure_time,job_title_id, job_title_name, old_user_id) values (now(), now(), "15205756810", "8fb4c89956827c7c950423e3d3bf70f1", "杨洋", "", "杨洋","M", "15205756810", "", "", "", "","", "1970-01-01 00:00:01", "127.0.0.1", "156","服务中心", "59", 21, "21", "1", "1970-01-01 00:00:01","0", "", "776");
COMMIT;
