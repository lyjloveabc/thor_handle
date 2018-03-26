"""
itl_company
zones
"""
from handle.global_setting import DEFAULT_DB_ENV


class Check:
    def __init__(self, dao):
        self.dao = dao

    def h(self):
        # 检验职能处理 #
        self.check_role()

        # 检验部门处理 #
        self.check_category()

    def check_role(self):
        old_data = self.dao.get_all('SELECT user.id AS uId, role_code AS rCode FROM user LEFT JOIN user_role_relation ON user.id = user_role_relation.user_id;')
        old_map = dict()
        for old in old_data:
            if old['uId'] not in old_map:
                old_map[old['uId']] = list()
            old_map[old['uId']].append(old['rCode'])

        new_data = self.dao.get_all('SELECT user.id AS uId, r.zone_id AS rZone, r.role_code AS rCode FROM user LEFT JOIN itl_user_role_relation r ON r.user_id = user.id;')
        new_map = dict()
        for new in new_data:
            if new['uId'] not in new_map:
                new_map[new['uId']] = set()
            new_map[new['uId']].add(new['rCode'])

        except_data = set()
        for k, v in old_map.items():
            for item in v:
                if item in new_map[k]:
                    pass
                else:
                    print('no: ', k, item)
                    except_data.add(str(k))

        except_zone = self.dao.get_all('SELECT id, zone_id FROM user WHERE id IN ({ids}) and zone_id not in (-1 ,1);'.format(ids=','.join(except_data)))
        for row in except_zone:
            print(row['id'], row['zone_id'])

    def check_category(self):
        zone_data = self.dao.get_all('SELECT user_id AS uId, zone_id AS zId FROM itl_user_zone_relation;')
        zone_map = dict()
        for zone in zone_data:
            if zone['uId'] not in zone_map:
                zone_map[zone['uId']] = set()
            zone_map[zone['uId']].add(zone['zId'])

        old_data = self.dao.get_all('SELECT id AS uId, category_id AS cId, category_name AS cName FROM user;')
        old_map = dict()
        for old in old_data:
            old_map[old['uId']] = old['cName']

        new_data = self.dao.get_all('SELECT user_id AS uId, zone_id AS zId, zone_category_id AS cId, zone_category_name AS cName FROM itl_user_category_relation;')
        new_map = dict()
        for new in new_data:
            new_map[str(new['uId']) + '-' + str(new['zId'])] = new['cName']

        except_data = set()
        for k, v in old_map.items():
            if k not in zone_map:
                continue
            for zone in zone_map[k]:
                key = str(k) + '-' + str(zone)

                if key not in new_map:
                    continue

                if v == new_map[key]:
                    pass
                else:
                    print('no: ', k, v, key)
                    except_data.add(str(k))


if __name__ == '__main__':
    check = Check(DEFAULT_DB_ENV)
    check.h()
