import requests
import json

from utils.db.daoUtil import DaoUtils
from utils.db.mysql.mySQLConfig import MySQLConfig


class PatrolSimple:
    def __init__(self):
        self.dao = DaoUtils(**{'dbType': 'MySQL', 'config': MySQLConfig.localhost()})

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
        delete_zone_task_ids = set()
        delete_user_task_ids = set()

        for row in data_db:
            delete_zone_task_ids.add(row['zt_id'])

            if row['ut_id'] is not None:
                delete_user_task_ids.add(row['ut_id'])

                if row['zone_id'] in task_cfg:
                    task_cfg[row['zone_id']]['user_ids'].add(row['user_id'])

                    if row['zt_id'] in task_cfg[row['zone_id']]['zt_ids']:
                        if row['overdue_time'] == 1:
                            task_cfg[row['zone_id']]['day_shift'] += 1
                        elif row['overdue_time'] == -1:
                            task_cfg[row['zone_id']]['night_shift'] += 1
                    else:
                        task_cfg[row['zone_id']]['zt_ids'].add(row['zt_id'])
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

        param = {
            'delZtIds': list(delete_zone_task_ids),
            'delUtIds': list(delete_user_task_ids)
        }
        param_sub = list()

        for key, value in task_cfg.items():
            pgf_item = {
                'zoneId': key,
                'pgc': [
                    {
                        'groupName': 'ALL_RANDOM',
                        'routeIds': [],
                        'staffIds': list(value['user_ids']),
                        'dayShiftCount': value['day_shift'],
                        'nightShiftCount': value['night_shift'],
                    }
                ]
            }
            param_sub.append(pgf_item)
        param['add'] = param_sub

        print(json.dumps(param))

        headers = {'content-type': 'application/json'}
        # requests.post("http://premanager.itianluo.cn/patrol/oldDataHandle?token=092ef9338413437abdf58e9560a0842a", headers=headers, data=json.dumps(param))
        requests.post("http://manager.itianluo.cn/patrol/oldDataHandle?token=092ef9338413437abdf58e9560a0842a", headers=headers, data=json.dumps(param))


if __name__ == '__main__':
    patrol = PatrolSimple()
    patrol.handle()
