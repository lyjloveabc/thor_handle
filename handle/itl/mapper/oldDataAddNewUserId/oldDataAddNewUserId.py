"""
因为管家端迁移，老的数据用的是 admin_employee 的ID，新加的user_id字段为空
需要通过手机号，对应找到新的user表的ID，写到新数据里面去
卧槽：上面的说明写着写着发现，只要一个sql就搞定了。MMP
"""


class OldDataAddNewUserId:
    def __init__(self):
        pass

    def handle(self):
        pass


if __name__ == '__main__':
    oldDataAddNewUserIdObject = OldDataAddNewUserId()
    oldDataAddNewUserIdObject.handle()
