BEGIN;
insert into user(gmt_create, gmt_modify, account, password, name, identity_card, nickname,sex, mobile, avatar_url, address, email, emergency_contact,emergency_mobile, last_login_time, last_login_ip, category_id,category_name, company_id, zone_id, zone_ids, is_on_job, departure_time,job_title_id, job_title_name, old_user_id) values (now(), now(), "15958122083", "5514a7da9c4965f51903bc71d2bffa01", "张利玲", "422822196306243021", "张利玲","F", "15958122083", "", "滨文苑", "", "曾发喜","", "1970-01-01 00:00:01", "127.0.0.1", "202","清洁", "76", 26, "26", "1", "1970-01-01 00:00:01","0", "", "239");
COMMIT;