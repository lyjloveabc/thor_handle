"""
ImportSomeUser 脚本需要的 sql
生成的第一条sql是查询
"""


class ImportSomeUserSql:
    @staticmethod
    def handle(mobile_group):
        if len(mobile_group) < 1:
            return

        sql_user = 'select count(1) from user where mobile in ('

        sql = 'select admin_employee.*, job_post.`name` ' \
              'from admin_employee left join job_post on job_post.id = admin_employee.job_post_id ' \
              'where admin_employee.mobile in ('

        print('查询user表是否已经存在:')
        print(ImportSomeUserSql.get_sql(sql_user, mobile_group))

        print()

        print('获取adminEmployee:')
        print(ImportSomeUserSql.get_sql(sql, mobile_group))

    @staticmethod
    def get_sql(sql, mobile_group):
        for mobile in mobile_group:
            sql += '"' + mobile + '", '

        sql = sql[:-2] + ');'
        return sql


if __name__ == '__main__':
    mobiles = ['1111', '2222']

    handle = ImportSomeUserSql()
    handle.handle(mobiles)
