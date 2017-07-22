BEGIN;
insert into user(gmt_create, gmt_modify, account, password, name, identity_card, nickname,sex, mobile, avatar_url, address, email, emergency_contact,emergency_mobile, last_login_time, last_login_ip, category_id,category_name, company_id, zone_id, zone_ids, is_on_job, departure_time,job_title_id, job_title_name, old_user_id) values (now(), now(), "15068147122", "b07dfadd188e95771f8bdfea92b76f7f", "郜亚欢", "", "郜亚欢","F", "15068147122", "", "", "", "","", "1970-01-01 00:00:01", "127.0.0.1", "166","服务中心", "59", 22, "22", "1", "1970-01-01 00:00:01","0", "00/00/0000 00:00:00", "964");
COMMIT;
