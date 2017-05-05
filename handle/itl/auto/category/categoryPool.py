"""
小区分类池
select title from admin_services_type order by id;
"""


class CategoryPool(object):
    BASE_PATH = 'file/'

    def __init__(self):
        pass

    @staticmethod
    def handle(name_group):
        if len(name_group) < 1:
            return

        print('BEGIN;')
        for name in name_group:
            sql = 'insert into itl_category_pool(gmt_create, gmt_modify, name) values(now(), now(), "' + name + '");'
            print(sql)
        print('COMMIT;')


if __name__ == '__main__':
    data = list()

    with open(CategoryPool.BASE_PATH + 'category_pool_temp.txt', 'r') as f:
        for line in f.readlines():
            data.append(line[:-1])

    handle = CategoryPool()
    handle.handle(data)
