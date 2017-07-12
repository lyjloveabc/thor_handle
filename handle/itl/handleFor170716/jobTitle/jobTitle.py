from handle.itl.handleFor170716.dbUtil import DbUtil
from handle.itl.handleFor170716.jobTitle.jobTitleData import JobTitleData


class JobTitle:
    def __init__(self, *args, **kw):
        self.dbUtil = kw['dbUtil']

        self.base_sql = "INSERT INTO itl_job_title (id, gmt_create, gmt_modify, name, duties, remark, type) " \
                        " VALUES('{id}', now(), now(), '{name}', '{duties}', '{remark}', '{type}');"

    def handle(self):
        self._add()

    def _add(self):
        sql_define = list()
        for row in JobTitleData.JOB_TITLE:
            sql_define.append(self.base_sql.format(id=row['id'], name=row['name'], duties=row['duties'], remark=row['remark'], type=row['type']))
        self.dbUtil.out_sql(sql_define, '添加添加岗位')
        self.dbUtil.exe_on_db(sql_define)


if __name__ == '__main__':
    handle = JobTitle(**{'dbUtil': DbUtil()})
    handle.handle()
