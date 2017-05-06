"""
5月初，用户迁移，产生了id不一致的问题
该脚本把线上已经有的数据，id转换成新的迁移后的id
迁移前的线上的用户数据：select id, account, name from user;
钱以后的线下的用户数据：
"""


class IdTransformForUserMove:
    def __init__(self):
        pass

    def handle(self):
        pass


if __name__ == '__main__':
    idTransformForUserMove = IdTransformForUserMove()
    idTransformForUserMove.handle()
