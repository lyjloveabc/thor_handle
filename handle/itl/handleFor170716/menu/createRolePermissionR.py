"""

"""
import os

from utils.db.daoUtil import DaoUtils
from utils.db.mysql.mySQLConfig import MySQLConfig


class CreateRolePermissionR:
    BASE_PATH = 'file/'

    def __init__(self):
        self.dao = DaoUtils(**{'dbType': 'MySQL', 'config': MySQLConfig.inner()})

        if not os.path.exists(CreateRolePermissionR.BASE_PATH):
            os.mkdir(CreateRolePermissionR.BASE_PATH)

    def handle(self):
        role_codes = self.dao.get_all('select code from role order by id;')
        permissions = self.dao.get_all('select code from permission where menu_kind in ("COMMONLY_TOOL", "HOUSEKEEPER_MY_TAB", "HOUSEKEEPER");')

        with open(CreateRolePermissionR.BASE_PATH + 'createRolePermissionR_out.sql', 'w') as f:
            f.write('BEGIN;\n')

            for row in role_codes:
                for record in permissions:
                    sql = 'insert into role_permission_relation(gmt_create, gmt_modify, permission_code, role_code) ' \
                          'values (now(), now(), "' + record['code'] + '", "' + row['code'] + '");'
                    f.write(sql + '\n')

            f.write('COMMIT;\n')


if __name__ == '__main__':
    handle = CreateRolePermissionR()
    handle.handle()
