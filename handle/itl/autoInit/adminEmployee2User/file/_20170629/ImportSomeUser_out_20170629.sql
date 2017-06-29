BEGIN;
insert into user(gmt_create, gmt_modify, account, password, name, identity_card, nickname,sex, mobile, avatar_url, address, email, emergency_contact,emergency_mobile, last_login_time, last_login_ip, category_id,category_name, company_id, zone_id, zone_ids, is_on_job, departure_time,job_title_id, job_title_name, old_user_id) values (now(), now(), "18800001234", "403636c29602a15b5ad56d1ab92affd6", "张三", "", "张三","M", "18800001234", "", "", "", "","", "1970-01-01 00:00:01", "127.0.0.1", "17","其他", "44", 2, "2", "1", "1970-01-01 00:00:01","0", "06/29/2017 11:36:56", "522");
COMMIT;
