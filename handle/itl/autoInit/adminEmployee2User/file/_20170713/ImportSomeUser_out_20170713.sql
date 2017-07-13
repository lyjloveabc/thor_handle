BEGIN;
insert into user(gmt_create, gmt_modify, account, password, name, identity_card, nickname,sex, mobile, avatar_url, address, email, emergency_contact,emergency_mobile, last_login_time, last_login_ip, category_id,category_name, company_id, zone_id, zone_ids, is_on_job, departure_time,job_title_id, job_title_name, old_user_id) values (now(), now(), "15336537511", "1661cb32ac4f842574847e6c66478fe1", "马艳菲", "", "马艳菲","F", "15336537511", "", "", "", "","", "1970-01-01 00:00:01", "127.0.0.1", "246","服务中心", "84", 29, "29", "1", "1970-01-01 00:00:01","0", "07/13/2017 10:08:17", "986");
COMMIT;
