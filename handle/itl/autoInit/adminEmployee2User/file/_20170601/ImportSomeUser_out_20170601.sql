BEGIN;
insert into user(gmt_create, gmt_modify, account, password, name, identity_card, nickname,sex, mobile, avatar_url, address, email, emergency_contact,emergency_mobile, last_login_time, last_login_ip, category_id,category_name, company_id, zone_id, zone_ids, is_on_job, departure_time,job_title_id, job_title_name, old_user_id) values (now(), now(), "18966668888", "f246c90fb548b1160738cbf9f533dcce", "杨任", "", "杨任","M", "18966668888", "", "", "", "","", "1970-01-01 00:00:01", "127.0.0.1", "176","服务中心", "63", 23, "23", "1", "1970-01-01 00:00:01","0", "00/00/0000 00:00:00", "857");
insert into user(gmt_create, gmt_modify, account, password, name, identity_card, nickname,sex, mobile, avatar_url, address, email, emergency_contact,emergency_mobile, last_login_time, last_login_ip, category_id,category_name, company_id, zone_id, zone_ids, is_on_job, departure_time,job_title_id, job_title_name, old_user_id) values (now(), now(), "18966668889", "d8ab34c7b400e988999daf3104de0669", "杨任", "", "杨任","M", "18966668889", "", "", "", "","", "1970-01-01 00:00:01", "127.0.0.1", "186","服务中心", "68", 24, "24", "1", "1970-01-01 00:00:01","0", "00/00/0000 00:00:00", "858");
COMMIT;


update user set password = (select password from admin_employee where mobile = '15088532883') where account = '15088532883'


13516816716
13819163873
15857172554
15958028212
13967120605
13812289135
13968070555
15925677587
15205756810)