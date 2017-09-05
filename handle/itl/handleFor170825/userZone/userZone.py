"""
处理人员小区关系数据
SELECT
    user.id, user.zone_id, user.zone_ids, count(user.id)
FROM
    user
        LEFT JOIN
    user_role_relation ON user_role_relation.user_id = user.id
WHERE
    user_role_relation.role_code NOT IN ('物业公司管理员' , '后台项目管理员', '小二') and user.zone_id > 0
GROUP BY user.id;
"""
from utils.constant.constant import Constant
from utils.db.daoUtil import DaoUtils
from utils.db.mysql.mySQLConfig import MySQLConfig


class UserZone:
    _BASE_SQL = 'INSERT INTO itl_user_zone_relation (created_time, modified_time, user_id, zone_id) VALUES (now(), now(), "{userId}", "{zoneId}");'

    def __init__(self):
        self.dao = DaoUtils(**{'dbType': 'MySQL', 'config': MySQLConfig.localhost()})

    def handle(self):
        data = self.dao.get_all(
            """
            SELECT
            user.id, user.zone_id, user.zone_ids, count(user.id)
            FROM
            user
            LEFT JOIN
            user_role_relation ON user_role_relation.user_id = user.id
            WHERE
            user_role_relation.role_code NOT IN ('物业公司管理员' , '后台项目管理员', '小二') AND user.zone_id > 0
            GROUP BY user.id;
            """
        )
        print(len(data))

        print(Constant.SQL_BEGIN)
        for temp in data:
            zone_ids = str(temp['zone_ids']).split(',')
            for zone_id in zone_ids:
                print(UserZone._BASE_SQL.format(userId=temp['id'], zoneId=zone_id))
        print(Constant.SQL_COMMIT)


if __name__ == '__main__':
    obj = UserZone()
    obj.handle()
