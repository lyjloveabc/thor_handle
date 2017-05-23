BEGIN;
insert into user(gmt_create, gmt_modify, account, password, name, identity_card, nickname,sex, mobile, avatar_url, address, email, emergency_contact,emergency_mobile, last_login_time, last_login_ip, category_id,category_name, company_id, zone_id, zone_ids, is_on_job, departure_time,job_title_id, job_title_name, old_user_id) values (now(), now(), "15055402387", "f3bff7e836604e4113d7a74aa8cc5e56", "彭进林", "", "彭进林","M", "15055402387", "", "", "", "","", "1970-01-01 00:00:01", "127.0.0.1", "184","安保", "74", 24, "24", "1", "1970-01-01 00:00:01","0", "", "849");
COMMIT;
