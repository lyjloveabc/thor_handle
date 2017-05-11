BEGIN;
insert into user(gmt_create, gmt_modify, account, password, name, identity_card, nickname,sex, mobile, avatar_url, address, email, emergency_contact,emergency_mobile, last_login_time, last_login_ip, category_id,category_name, company_id, zone_id, zone_ids, is_on_job, departure_time,job_title_id, job_title_name, old_user_id) values (now(), now(), "15157116059", "299d063b400ad701ed7d6d7ecef18080", "常均友", "", "常均友","M", "15157116059", "", "", "", "","", "1970-01-01 00:00:01", "127.0.0.1", "14","安保", "37", 2, "2", "1", "1970-01-01 00:00:01","0", "夜班西门2号岗", "793");
COMMIT;
