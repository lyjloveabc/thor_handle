BEGIN;
update user set gmt_modify = now(), password = "5514a7da9c4965f51903bc71d2bffa01", name = "张利玲",identity_card = "422822196306243021", nickname = "张利玲",sex = "F", mobile = "15958122083", avatar_url = "",address = "滨文苑", email = "", emergency_contact = "曾发喜",emergency_mobile = "", last_login_time = "1970-01-01 00:00:01",last_login_ip = "127.0.0.1", category_id = "202",category_name = "清洁", company_id = "76",zone_id = "26", zone_ids = "26", is_on_job = "1",departure_time = "1970-01-01 00:00:01", job_title_id = "0",job_title_name = "", old_user_id = "239" where account = "15958122083";
COMMIT;
