"""
5月初，用户迁移，产生了id不一致的问题
该脚本把线上已经有的数据，id转换成新的迁移后的id
迁移前的线上的用户数据:select id, account, name from user;
receipt:select id, operator_id, operator_name from receipt;
"""
from utils.constant.constant import Constant


class IdTransformForUserMove:
    def __init__(self):
        pass

    def handle(self):
        receipt_sql = 'update receipt set operator_id = {new_operator_id}, operator_name = {new_operator_name} ' \
                      'where operator_id = {ole_operator_id};'

        online_user_before = IdTransformForUserMove.get_user(Constant.BASE_PATH + 'onlineUser_20170506.txt')
        offline_user_after = IdTransformForUserMove.get_user_after(Constant.BASE_PATH + 'offlineUser_20170506.txt')

        receipt_group = IdTransformForUserMove.get_receipt(Constant.BASE_PATH + 'receipt_20170506.txt')

        for receipt in receipt_group:
            old_id = receipt['operator_id']
            account = online_user_before[old_id]['account']
            new_id = offline_user_after[account]['id']
            new_name = offline_user_after[account]['name']
            print(receipt_sql.format(new_operator_id=new_id, new_operator_name=new_name, ole_operator_id=old_id))

    @staticmethod
    def get_user(file_name):
        user_group = dict()
        with open(file_name, 'r') as f:
            for line in f.readlines():
                line_split = line[:-1].split(';')
                item = {
                    'id': line_split[0],
                    'account': line_split[1],
                    'name': line_split[2]
                }
                user_group[item['id']] = item
        return user_group

    @staticmethod
    def get_user_after(file_name):
        user_group = dict()
        with open(file_name, 'r') as f:
            for line in f.readlines():
                line_split = line[:-1].split(';')
                item = {
                    'id': line_split[0],
                    'account': line_split[1],
                    'name': line_split[2]
                }
                user_group[item['account']] = item
        return user_group

    @staticmethod
    def get_receipt(file_name):
        receipt_group = list()
        with open(file_name, 'r') as f:
            for line in f.readlines():
                line_split = line[:-1].split(';')
                item = {
                    'id': line_split[0],
                    'operator_id': line_split[1],
                    'operator_name': line_split[2]
                }
                receipt_group.append(item)
        return receipt_group


if __name__ == '__main__':
    idTransformForUserMove = IdTransformForUserMove()
    idTransformForUserMove.handle()
