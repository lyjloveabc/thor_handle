"""
SELECT * FROM duty WHERE `jcid` = 0 AND `unfinish` > 0 AND `finish_time` > unix_timestamp() ORDER BY id DESC;

SELECT
user.id, user.name,
duty.zone_id, duty.content, duty.start_time, duty.finish_time, duty.important,
exe.id, exe.name,
duty_to.content
FROM duty
LEFT JOIN duty_to ON duty_to.duty_id = duty.id
LEFT JOIN admin_employee ON admin_employee.id = duty.employee_id
LEFT JOIN user ON user.account = admin_employee.mobile
LEFT JOIN admin_employee exeAdmin ON exeAdmin.id = duty_to.employee_id
LEFT JOIN user exe ON exe.account = exeAdmin.mobile
WHERE duty.jcid = 0 AND duty.unfinish > 0 AND duty.finish_time > unix_timestamp()
AND duty_to.status = 0
ORDER BY duty.id DESC;
"""
import json
from datetime import datetime


class DutyToTask:
    _INSERT_LAUNCH_SQL = 'INSERT INTO itl_launch_task(id, created_time, modified_time, is_daily_task, launch_user_id, zone_id, daily_task_owner_user_id, ' \
                         + 'code, type, content, standard, rate, start_time, overdue_time, is_emergent, images, is_received, sort_num) ' \
                         + 'VALUES("{id}", now(), now(), 0, "{launch_user_id}", "{zone_id}", 0, "{code}", "{type}", "{content}", "{standard}", ' \
                         + '"{rate}", now(), "{overdue_time}", "{is_emergent}", "{images}", 1, 1);'

    _INSERT_DO_SQL = 'INSERT INTO itl_do_task(created_time, modified_time, owner_user_id, executor_user_id, launch_task_id, zone_id, ' \
                     + 'content, images, status) ' \
                     + 'VALUES(now(), now(), "{owner_user_id}", "{executor_user_id}", "{launch_task_id}", "{zone_id}", ' \
                       '"{content}", "{images}", "{status}");'

    def __init__(self):
        pass

    def handle(self):
        with open('duty_data.json') as json_file:
            duty_data = json.load(json_file)
            index = 1000
            for row in duty_data:
                sql = DutyToTask._INSERT_LAUNCH_SQL.format(id=index, launch_user_id=row['launch_user_id'], zone_id=row['zone_id'], code='', type='1B',
                                                           content=row['content'], standard='', rate='', overdue_time=datetime.fromtimestamp(row['finish_time']),
                                                           is_emergent=row['important'], images='')
                sql2 = DutyToTask._INSERT_DO_SQL.format(owner_user_id=row['exe_user_id'], executor_user_id=row['exe_user_id'], launch_task_id=index,
                                                        zone_id=row['zone_id'], content='', images='', status=1)
                print(sql)
                print(sql2)


if __name__ == '__main__':
    obj = DutyToTask()
    obj.handle()
