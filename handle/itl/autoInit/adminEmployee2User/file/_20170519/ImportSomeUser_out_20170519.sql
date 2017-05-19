BEGIN;
insert into user(gmt_create, gmt_modify, account, password, name, identity_card, nickname,sex, mobile, avatar_url, address, email, emergency_contact,emergency_mobile, last_login_time, last_login_ip, category_id,category_name, company_id, zone_id, zone_ids, is_on_job, departure_time,job_title_id, job_title_name, old_user_id) values (now(), now(), "13738178421", "017afe8f2aa52f534bd587ae9ab14ad1", "邹志鹏", "", "邹志鹏","M", "13738178421", "", "", "", "","", "1970-01-01 00:00:01", "127.0.0.1", "164","安保", "61", 22, "22", "1", "1970-01-01 00:00:01","0", "", "801");
COMMIT;
