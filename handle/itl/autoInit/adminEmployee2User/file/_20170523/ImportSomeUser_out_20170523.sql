BEGIN;
insert into user(gmt_create, gmt_modify, account, password, name, identity_card, nickname,sex, mobile, avatar_url, address, email, emergency_contact,emergency_mobile, last_login_time, last_login_ip, category_id,category_name, company_id, zone_id, zone_ids, is_on_job, departure_time,job_title_id, job_title_name, old_user_id) values (now(), now(), "13989841017", "4edac4bef40dcfa043c52682ef629b28", "陈潇潇", "", "陈潇潇","F", "13989841017", "", "", "", "","", "1970-01-01 00:00:01", "127.0.0.1", "216","服务中心", "73", 27, "27", "1", "1970-01-01 00:00:01","0", "", "846");
COMMIT;
