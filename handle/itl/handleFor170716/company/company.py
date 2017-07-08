"""

"""
from handle.itl.handleFor170716.company.data.companyData import CompanyData
from handle.itl.handleFor170716.dbUtil import DbUtil


class Company:
    _BASE_SQL = 'INSERT INTO itl_company' \
                '(id, company_name, status, comment, created_time, modified_time, modified_by, alias) ' \
                'VALUES ' \
                '("{id}", "{company_name}", "{status}", "{comment}", now(), now(), "{modified_by}", "{alias}");'

    def __init__(self, *args, **kw):
        self.dbUtil = kw['dbUtil']

    def handle(self):
        self._add()

    def _add(self):
        sql_define = list()

        for row in CompanyData.COMPANY:
            sql = Company._BASE_SQL.format(id=row['id'], company_name=row['company_name'], status=row['status'], comment=row['company_name'], modified_by=0, alias=row['company_name'])
            sql_define.append(sql)

        self.dbUtil.out_sql(sql_define, '')
        self.dbUtil.exe_on_db(sql_define)


if __name__ == '__main__':
    handle = Company(**{'dbUtil': DbUtil()})
    handle.handle()
