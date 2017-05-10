BEGIN;
insert into user(gmt_create, gmt_modify, account, password, name, identity_card, nickname,sex, mobile, avatar_url, address, email, emergency_contact,emergency_mobile, last_login_time, last_login_ip, category_id,category_name, company_id, zone_id, zone_ids, is_on_job, departure_time,job_title_id, job_title_name, old_user_id) values (now(), now(), "17075203536", "1cc0b7cf6b956741062efe60611c85a5", "侯罗营", "", "侯罗营","M", "17075203536", "", "", "", "","", "1970-01-01 00:00:01", "127.0.0.1", "11","绿化", "21", 2, "2", "1", "1970-01-01 00:00:01","0", "绿化工", "792");
COMMIT;
