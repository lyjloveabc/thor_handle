BEGIN;
insert into user(gmt_create, gmt_modify, account, password, name, identity_card, nickname,sex, mobile, avatar_url, address, email, emergency_contact,emergency_mobile, last_login_time, last_login_ip, category_id,category_name, company_id, zone_id, zone_ids, is_on_job, departure_time,job_title_id, job_title_name, old_user_id) values (now(), now(), "17757547192", "cd5a101eaac306e5afeafc1256b9bab4", "郑珂", "", "郑珂","M", "17757547192", "", "", "", "","", "1970-01-01 00:00:01", "127.0.0.1", "37","其他", "67", 9, "9", "1", "1970-01-01 00:00:01","0", "", "760");
insert into user(gmt_create, gmt_modify, account, password, name, identity_card, nickname,sex, mobile, avatar_url, address, email, emergency_contact,emergency_mobile, last_login_time, last_login_ip, category_id,category_name, company_id, zone_id, zone_ids, is_on_job, departure_time,job_title_id, job_title_name, old_user_id) values (now(), now(), "15664205670", "27fe9427f15c594a3a89f3b3144ef27b", "李亚琼", "", "李亚琼","F", "15664205670", "employee/170505/1493989272.jpg", "", "", "","", "1970-01-01 00:00:01", "127.0.0.1", "166","服务中心", "59", 22, "22", "1", "1970-01-01 00:00:01","0", "", "773");
COMMIT;