"""
用户迁移
"""


class OldUserToNewUser(object):
    __BASE_PATH = 'file/'

    def __init__(self):
        self.base_sql = 'update user ' \
                        'set avatar_url = "{avatar_url}", category_id = {category_id}, category_name = "{category_name}", job_title_name = "{job_title_name}" ' \
                        'where id = {id};'

    def handle(self):
        old = dict()
        with open(OldUserToNewUser.__BASE_PATH + 'admin_employee.txt', 'r') as f:
            for line in f.readlines():
                temp = line[:-1].split(',')
                mobile = temp[0]
                category_id = temp[2]
                category_name = temp[3]

                if category_id == 0 or category_id == '':
                    category_id = 7
                    category_name = '其他'
                old[mobile] = {
                    'avatar_url': temp[1],
                    'category_id': category_id,
                    'category_name': category_name,
                    'job_title_name': temp[4]
                }

        print('BEGIN;')
        with open(OldUserToNewUser.__BASE_PATH + 'user.txt', 'r') as f:
            for line in f.readlines():
                temp = line[:-1].split(',')
                id = temp[0]
                mobile = temp[1]
                if temp[1] in old:
                    print(self.base_sql.format(avatar_url=old[mobile]['avatar_url'], category_id=old[mobile]['category_id'], category_name=old[mobile]['category_name'],
                                               job_title_name=old[mobile]['job_title_name'], id=id))
        print('COMMIT;')


if __name__ == '__main__':
    handle = OldUserToNewUser()
    handle.handle()

    # select
    # admin_employee.mobile, admin_employee.avtar, admin_services_type.id, admin_services_type.title,
    # job_post.name
    # from
    # admin_employee left join job_post on admin_employee.job_post_id = job_post.id
    # left join admin_services_type on admin_employee.type = admin_services_type.id
