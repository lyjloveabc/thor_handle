"""
sql
"""
from utils.constant.constant import Constant


class OldUserSql:
    @staticmethod
    def handle(mobile_group):
        if len(mobile_group) < 1:
            return

        sql_user = 'select * from user where mobile in ('

        sql = 'select admin_employee.*, job_post.`name` ' \
              'from admin_employee left join job_post on job_post.id = admin_employee.job_post_id ' \
              'where admin_employee.mobile in ('

        print('查询user表是否已经存在:')
        print(OldUserSql.get_sql(sql_user, mobile_group))

        print()

        print('获取adminEmployee:')
        print(OldUserSql.get_sql(sql, mobile_group))

    @staticmethod
    def get_sql(sql, mobile_group):
        for mobile in mobile_group:
            sql += '"' + mobile + '", '

        sql = sql[:-2] + ');'
        return sql


if __name__ == '__main__':
    # mobiles = list()
    #
    # with open(Constant.BASE_PATH + '_20170607/华隆.txt', 'r') as f:
    #     for line in f.readlines():
    #         mobiles.append(line[:-1])
    mobiles = [
        '18800001234',
    ]

    for item in mobiles:
        print(item)

    handle = OldUserSql()
    handle.handle(mobiles)

    # a = [15088532883,
    #      13516816716,
    #      13819163873,
    #      15857172554,
    #      15958028212,
    #      13967120605,
    #      13812289135,
    #      13968070555,
    #      15925677587,
    #      15205756810]
    # for aaa in a:
    #     print("update user set password = (select password from admin_employee where mobile = '"
    #           + str(aaa) + "') where account = '" + str(aaa) + "';")

# 更改：杨桂银13306518942
# 离职：艾厚玉17858840882
# 翟学强13857167765


# 赵克义15700184129
# 宋亚东13333678031
# 石豪威15737751132
# 张祥明13989821227
# 赵孟学13592082991
# 郭明宇17621131427
# 朱捡仁18879940477
# 张中仁15167186699
