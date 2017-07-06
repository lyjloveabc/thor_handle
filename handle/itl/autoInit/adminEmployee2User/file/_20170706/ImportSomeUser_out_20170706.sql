BEGIN;
insert into user(gmt_create, gmt_modify, account, password, name, identity_card, nickname,sex, mobile, avatar_url, address, email, emergency_contact,emergency_mobile, last_login_time, last_login_ip, category_id,category_name, company_id, zone_id, zone_ids, is_on_job, departure_time,job_title_id, job_title_name, old_user_id) values (now(), now(), "18936723312", "a27a40d64a9285db8ca49b1bb039959c", "周雯雯", "", "周雯雯","F", "18936723312", "", "", "", "","", "1970-01-01 00:00:01", "127.0.0.1", "206","服务中心", "73", 26, "26", "1", "1970-01-01 00:00:01","0", "00/00/0000 00:00:00", "949");
COMMIT;
