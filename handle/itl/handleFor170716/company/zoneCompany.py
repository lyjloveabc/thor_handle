"""

"""
from handle.itl.handleFor170716.company.data.companyData import CompanyData
from handle.itl.handleFor170716.dbUtil import DbUtil


class ZoneCompany:
    _BASE_SQL = 'UPDATE zones SET company_id = "{company_id}" WHERE id = "{id}";'

    def __init__(self, *args, **kw):
        self.dbUtil = kw['dbUtil']

    def handle(self):
        self._add()

    def _add(self):
        sql_define = list()

        for row in CompanyData.ZONE:
            sql = ZoneCompany._BASE_SQL.format(company_id=row['company_id'], id=row['id'])
            sql_define.append(sql)

        self.dbUtil.out_sql(sql_define, '更新现有小区的公司名称')
        self.dbUtil.exe_on_db(sql_define)


if __name__ == '__main__':
    handle = ZoneCompany(**{'dbUtil': DbUtil()})
    handle.handle()
