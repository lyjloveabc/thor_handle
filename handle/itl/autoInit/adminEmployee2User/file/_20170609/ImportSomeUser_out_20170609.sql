BEGIN;
insert into user(gmt_create, gmt_modify, account, password, name, identity_card, nickname,sex, mobile, avatar_url, address, email, emergency_contact,emergency_mobile, last_login_time, last_login_ip, category_id,category_name, company_id, zone_id, zone_ids, is_on_job, departure_time,job_title_id, job_title_name, old_user_id) values (now(), now(), "13588247481", "6d571af6b2d3d60c9e3bf5fb816e17aa", "方国峰", "", "方国峰","M", "13588247481", "employee/170609/1496999420.jpg", "", "", "","", "1970-01-01 00:00:01", "127.0.0.1", "224","安保", "81", 28, "28", "1", "1970-01-01 00:00:01","0", "00/00/0000 00:00:00", "918");
COMMIT;