import requests
from utils.db.daoUtil import DaoUtils
from utils.db.mysql.mySQLConfig import MySQLConfig


class Patrol:
    def __init__(self):
        self.dao = DaoUtils(**{'dbType': 'MySQL', 'config': MySQLConfig.localhost()})
        # self.delete_zone_task_sql = 'DELETE FROM itl_zone_task WHERE type = "1E" AND zone_id = {zone_id} AND id = {id};'
        self.delete_user_task = 'DELETE FROM itl_user_task WHERE zone_id = {zone_id} AND id = {id};'
        self.insert_group = 'INSERT INTO itl_patrol_group' \
                            ' (created_time, modified_time, zone_id, group_type, name, route_ids, user_ids, zone_task_ids, day_shift_count, night_shift_count, operator_id)' \
                            ' VALUES (now(), now(), {zone_id}, 2, "ALL_RANDOM", "", "{user_ids}", "{zone_task_ids}", {day_shift_count}, {night_shift_count}, 431);'
        self.insert_user_task = 'INSERT INTO itl_user_task (created_time, modified_time, zone_task_id, user_id)' \
                                ' VALUES (now(), now(), {zone_task_id}, {user_id});'
        self.insert_group_user = 'INSERT INTO itl_patrol_group_user (created_time, modified_time, zone_id, patrol_group_id, patrol_user_id, operator_id)' \
                                 ' VALUES (now(), now(), {zone_id}, {patrol_group_id}, {patrol_user_id}, 431);'

    def handle(self):
        data_db = self.dao.get_all("""
                    SELECT 
                    itl_zone_task.id AS zt_id,
                    itl_zone_task.overdue_time,
                    itl_zone_task.start_time,
                    itl_zone_task.zone_id,
                    itl_user_task.id AS ut_id,
                    itl_user_task.user_id
                    FROM itl_zone_task LEFT JOIN itl_user_task ON itl_user_task.zone_task_id = itl_zone_task.id
                    WHERE type = '1E' AND is_valid = 1
                    ORDER BY itl_zone_task.zone_id;
                  """)

        task_cfg = dict()
        # delete_zone_task = set()
        delete_user_task = set()

        for row in data_db:
            # delete_zone_task.add(self.delete_zone_task_sql.format(zone_id=row['zone_id'], id=row['zt_id']))
            delete_user_task.add(self.delete_user_task.format(zone_id=row['zone_id'], id=row['ut_id']))
            if row['zone_id'] in task_cfg:
                task_cfg[row['zone_id']]['zt_ids'].add(row['zt_id'])
                task_cfg[row['zone_id']]['user_ids'].add(row['user_id'])

                if row['overdue_time'] == 1:
                    task_cfg[row['zone_id']]['day_shift'] += 1
                elif row['overdue_time'] == -1:
                    task_cfg[row['zone_id']]['night_shift'] += 1
            else:
                day_shift = 0
                night_shift = 0
                user_ids = set()
                user_ids.add(row['user_id'])
                zt_ids = set()
                zt_ids.add(row['zt_id'])

                if row['overdue_time'] == 1:
                    day_shift = 1
                elif row['overdue_time'] == -1:
                    night_shift = 1

                task_cfg[row['zone_id']] = {
                    'zt_ids': zt_ids,
                    'user_ids': user_ids,
                    'day_shift': day_shift,
                    'night_shift': night_shift
                }

        data = dict()
        for row in task_cfg:
            print(row)

        requests.post("http://httpbin.org/post", data=data)


if __name__ == '__main__':
    patrol = Patrol()
    patrol.handle()
