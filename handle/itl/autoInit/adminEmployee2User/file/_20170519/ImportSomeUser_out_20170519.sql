BEGIN;
insert into user(gmt_create, gmt_modify, account, password, name, identity_card, nickname,sex, mobile, avatar_url, address, email, emergency_contact,emergency_mobile, last_login_time, last_login_ip, category_id,category_name, company_id, zone_id, zone_ids, is_on_job, departure_time,job_title_id, job_title_name, old_user_id) values (now(), now(), "18855928531", "9eacac13db0ba25cfb0493172aab2b4b", "徐庆阳", "", "徐庆阳","M", "18855928531", "", "", "", "","", "1970-01-01 00:00:01", "127.0.0.1", "174","安保", "65", 23, "23", "1", "1970-01-01 00:00:01","0", "", "804");
COMMIT;
