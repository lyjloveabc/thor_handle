"""
数据整理
"""


class UserRoleRelation:
    __BASE_PATH = 'file/'

    def __init__(self):
        self.base_sql = 'insert into user_role_relation(gmt_create, gmt_modify, user_id, role_code) values ' \
                        '(now(), now(), {user_id}, "{role_code}");'

    def handle(self):
        user_role_group = list()
        with open(UserRoleRelation.__BASE_PATH + 'user_role_relation.txt', 'r') as f:
            for line in f.readlines():
                temp = line[:-1].split(',')
                user_id = temp[0]
                role_code = temp[1]
                user_role_group.append({'user_id': user_id, 'role_code': role_code})

        print('BEGIN;')
        for user_role in user_role_group:
            print(self.base_sql.format(user_id=user_role['user_id'], role_code=user_role['role_code']))
        print('COMMIT;')


if __name__ == '__main__':
    handle = UserRoleRelation()
    handle.handle()

    # select
    # admin_employee.mobile, admin_employee.avtar, admin_services_type.id, admin_services_type.title,
    # job_post.name
    # from
    # admin_employee left join job_post on admin_employee.job_post_id = job_post.id
    # left join admin_services_type on admin_employee.type = admin_services_type.id
