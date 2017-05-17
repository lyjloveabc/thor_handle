BEGIN;
insert into user(gmt_create, gmt_modify, account, password, name, identity_card, nickname,sex, mobile, avatar_url, address, email, emergency_contact,emergency_mobile, last_login_time, last_login_ip, category_id,category_name, company_id, zone_id, zone_ids, is_on_job, departure_time,job_title_id, job_title_name, old_user_id) values (now(), now(), "15157145227", "cb56a5d9cbe8ddca2252553e2ab99e13", "王岩", "", "王岩","M", "15157145227", "", "", "", "","", "1970-01-01 00:00:01", "127.0.0.1", "44","安保", "35", 10, "10", "1", "1970-01-01 00:00:01","0", "白班大厅门岗", "798");
COMMIT;
