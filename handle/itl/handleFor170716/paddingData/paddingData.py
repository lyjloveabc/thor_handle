"""
填充数据
"""
from handle.itl.handleFor170716.dbUtil import DbUtil


class PaddingData:
    def __init__(self, *args, **kw):
        self.dbUtil = DbUtil()

    def handle(self):
        self._bill()
        self._insert_user_id()

    def _bill(self):
        sql_define = ["UPDATE BILL SET is_checked=1, financial_income=ought_amount;"]
        self.dbUtil.out_sql(sql_define, '所有已经存在的账单给新添加的is_checked、financial_income字段设置默认值')
        self.dbUtil.exe_on_db(sql_define)

    def _insert_user_id(self):
        self._sub_enter()
        self._repair()
        self._appraisal()
        self._summary_plan()
        self._bug_report()
        self._chat()

    def _sub_enter(self):
        sql_define = list()
        sub_enter = self.dbUtil.get_all_subscription_enter()
        for row in sub_enter:
            user_id = self.dbUtil.get_user_id(row['admin_employee_id'])
            sql_define.append("UPDATE subscription_enter SET user_id=" + str(user_id) + " WHERE id=" + str(row['id']) + ";")
        self.dbUtil.out_sql(sql_define, '所有的能耗录入，填充user_id')
        self.dbUtil.exe_on_db(sql_define)

    def _repair(self):
        sql_define = list()
        repair = self.dbUtil.get_all_repair()
        for row in repair:
            g_user_id = self.dbUtil.get_user_id(row['guid'])
            user_id = self.dbUtil.get_user_id(row['employee_id'])
            sql_define.append("UPDATE task SET guid=" + str(g_user_id) + ", employee_id=" + str(user_id) + " WHERE id=" + str(row['id']) + ";")
        self.dbUtil.out_sql(sql_define, '所有的task，填充user_id')
        self.dbUtil.exe_on_db(sql_define)

        sql_define = list()
        task_map = self.dbUtil.get_all_task_map()
        for row in task_map:
            user_id = self.dbUtil.get_user_id(row['uid'])
            sql_define.append("UPDATE task_map SET user_id=" + str(user_id) + " WHERE id=" + str(row['id']) + ";")
        self.dbUtil.out_sql(sql_define, '所有的task_map，填充user_id')
        self.dbUtil.exe_on_db(sql_define)

    def _appraisal(self):
        rows = self.dbUtil.get_about_appraisal()
        for row in rows:
            self._about_appraisal_do(row['table'], row['data'])

    def _summary_plan(self):
        sql_define = list()
        rows = self.dbUtil.get_all_summary_plan()
        for row in rows:
            user_id = self.dbUtil.get_user_id(row['employee_id'])
            sql_define.append("UPDATE summary_plan SET user_id=" + str(user_id) + " WHERE id=" + str(row['id']) + ";")
        self.dbUtil.out_sql(sql_define, '所有的总结计划，填充user_id')
        self.dbUtil.exe_on_db(sql_define)

    def _bug_report(self):
        sql_define = list()
        rows = self.dbUtil.get_all_bug_report()
        for row in rows:
            user_id = self.dbUtil.get_user_id(row['uid'])
            sql_define.append("UPDATE bug_report SET user_id=" + str(user_id) + " WHERE id=" + str(row['id']) + ";")
        self.dbUtil.out_sql(sql_define, 'bug_report，填充user_id')
        self.dbUtil.exe_on_db(sql_define)

    def _chat(self):
        sql_define = list()
        rows = self.dbUtil.get_all_chat()
        for row in rows:
            user = self.dbUtil.get_user(row['reply_id'])
            sql_define.append("UPDATE chat SET reply_id=" + str(user['id']) + ", reply_name='" + str(user['name']) + "' WHERE id=" + str(row['id']) + ";")
        self.dbUtil.out_sql(sql_define, 'bug_report，填充user_id')
        self.dbUtil.exe_on_db(sql_define)

    def _about_appraisal_do(self, table, data_list):
        sql_define = list()
        for row in data_list:
            user_id = self.dbUtil.get_user_id(row['eid'])
            sql_define.append("UPDATE " + table + " SET user_id=" + str(user_id) + " WHERE id=" + str(row['id']) + ";")
        self.dbUtil.out_sql(sql_define, table)
        self.dbUtil.exe_on_db(sql_define)


if __name__ == '__main__':
    handle = PaddingData()
    handle.handle()
