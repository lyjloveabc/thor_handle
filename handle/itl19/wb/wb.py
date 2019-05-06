import os
from decimal import *


class Wb:
    def __init__(self, source_bill_file, mapping_file):
        self.source_bill = Wb.read_source_bill(source_bill_file)  # 老的账单
        self.mapping = Wb.read_mapping(mapping_file)  # 新老账单对应关系
        self.mapping_keys = self.mapping.keys()  # 新老账单对应关系的老的账单ID

        self.not_in_new_bill = list()  # 老的账单没有在新的里面
        self.no_match = list()  # 没有在任何case里面
        self.match_many = list()  # 在多个case里面

        self.need_update = list()  # 最终需要更新的数据
        self.need_insert = list()  # 最终需要插入的数据

        self.sql_update_1 = 'UPDATE itl_finance_bill SET real_amount = {real_amount}, discount_amount = {discount_amount}, owe_amount = 0 WHERE id = {id};'
        self.sql_update_2 = 'UPDATE itl_finance_bill SET ought_amount = {ought_amount}, real_amount = {real_amount} , discount_amount = {discount_amount}, round_amount = 0, owe_amount = 0 WHERE id = {id};'
        self.sql_update_3 = """
                            UPDATE itl_finance_bill SET ought_amount = {ought_amount}, 
                            real_amount = {real_amount}, discount_amount = {discount_amount},
                            round_amount = 0, owe_amount = 0,
                            debtor_card_type = '手动处理',
                            debtor_card_no = '手动处理',
                            debtor_name = '手动处理',
                            debtor_mobile = '手动处理'
                            WHERE id = {id};
                            """
        self.sql_update_4 = """
                            UPDATE itl_finance_bill SET ought_amount = {ought_amount}, 
                            real_amount = 0, discount_amount = 0,
                            round_amount = 0, owe_amount = {ought_amount},
                            debtor_card_type = '手动处理',
                            debtor_card_no = '手动处理',
                            debtor_name = '手动处理',
                            debtor_mobile = '手动处理'
                            WHERE id = {id};
                            """
        self.sql_update_5 = "UPDATE itl_finance_bill SET debtor_card_type = '手动处理', debtor_card_no = '手动处理', debtor_name = '手动处理', debtor_mobile = '手动处理' WHERE id = {id};"
        self.sql_update_6 = """
                            UPDATE itl_finance_bill SET 
                            real_amount = {real_amount}, discount_amount = 0,
                            round_amount = 0, owe_amount = 0,
                            debtor_card_type = '手动处理',
                            debtor_card_no = '手动处理',
                            debtor_name = '手动处理',
                            debtor_mobile = '手动处理'
                            WHERE id = {id};
                            """

        self.sql_insert_2 = """
                            INSERT INTO `itl_finance_bill` 
                            (`gmt_create`, `gmt_modified`, `zone_id`, `subject_id`, `bill_period_id`, 
                            `start_day`, `end_day`, `ought_amount`, `real_amount`, `discount_amount`, `round_amount`, 
                            `owe_amount`, `estate_type`, `estate_id`, `debtor_card_type`, `debtor_card_no`, `debtor_name`, 
                            `debtor_mobile`, `zone_subject_id`) 
                            SELECT `gmt_create`, `gmt_modified`, `zone_id`, `subject_id`, `bill_period_id`, 
                            `start_day`, `end_day`, {ought_amount}, 0, 0, 0, 
                            {ought_amount}, `estate_type`, `estate_id`, `debtor_card_type`, `debtor_card_no`, `debtor_name`, 
                            `debtor_mobile`, `zone_subject_id` FROM itl_finance_bill WHERE id = {id};
                          """
        self.sql_insert_3_1 = """
                              INSERT INTO `itl_finance_bill` 
                            (`gmt_create`, `gmt_modified`, `zone_id`, `subject_id`, `bill_period_id`, 
                            `start_day`, `end_day`, `ought_amount`, `real_amount`, `discount_amount`, `round_amount`, 
                            `owe_amount`, `estate_type`, `estate_id`, `debtor_card_type`, `debtor_card_no`, `debtor_name`, 
                            `debtor_mobile`, `zone_subject_id`) 
                            SELECT `gmt_create`, `gmt_modified`, `zone_id`, `subject_id`, `bill_period_id`, 
                            `start_day`, `end_day`, {ought_amount}, 0, 0, 0, 
                            {ought_amount}, `estate_type`, `estate_id`, '手动处理', '手动处理', '手动处理', 
                            '手动处理', `zone_subject_id` FROM itl_finance_bill WHERE id = {id};
                             """
        self.sql_insert_3_2 = """
                                INSERT INTO `itl_finance_bill` 
                                (`gmt_create`, `gmt_modified`, `zone_id`, `subject_id`, `bill_period_id`, 
                                `start_day`, `end_day`, `ought_amount`, `real_amount`, `discount_amount`, `round_amount`, 
                                `owe_amount`, `estate_type`, `estate_id`, `debtor_card_type`, `debtor_card_no`, `debtor_name`, 
                                `debtor_mobile`, `zone_subject_id`) 
                                SELECT `gmt_create`, `gmt_modified`, `zone_id`, `subject_id`, `bill_period_id`, 
                                `start_day`, `end_day`, {ought_amount}, 0, 0, 0, 
                                {ought_amount}, `estate_type`, `estate_id`, 
                                `debtor_card_type`, `debtor_card_no`, `debtor_name`, `debtor_mobile`, 
                                `zone_subject_id` FROM itl_finance_bill WHERE id = {id};
                                """
        self.sql_insert_4 = """
                            INSERT INTO `itl_finance_bill` 
                            (`gmt_create`, `gmt_modified`, `zone_id`, `subject_id`, `bill_period_id`, 
                            `start_day`, `end_day`, `ought_amount`, `real_amount`, `discount_amount`, `round_amount`, 
                            `owe_amount`, `estate_type`, `estate_id`, `debtor_card_type`, `debtor_card_no`, `debtor_name`, 
                            `debtor_mobile`, `zone_subject_id`) 
                            SELECT `gmt_create`, `gmt_modified`, `zone_id`, `subject_id`, `bill_period_id`, 
                            `start_day`, `end_day`, {ought_amount}, 0, 0, 0, 
                            {ought_amount}, `estate_type`, `estate_id`, `debtor_card_type`, `debtor_card_no`, `debtor_name`, 
                            `debtor_mobile`, `zone_subject_id` FROM itl_finance_bill WHERE id = {id};
                            """

    def handle(self, path):
        for row in self.source_bill:
            if row['id'] in self.mapping_keys:
                many_time = list()
                update = list()
                insert = list()

                if row['id'] == '1809':
                    print(row['ought_amount'] == (row['real_amount'] + row['discount_money']))
                    print(row['ought_amount'])
                    print((row['real_amount'] + row['discount_money']))

                if row['ought_amount'] == (row['real_amount'] + row['discount_money']):
                    many_time.append(1)
                    update.append(
                        self.sql_update_1.format(
                            real_amount=row['real_amount'], discount_amount=row['discount_money'], id=self.mapping[row['id']]['new_id']
                        )
                    )

                if row['hang_up_bill_amount'] == 0 and row['ought_amount'] > (row['real_amount'] + row['discount_money']):
                    many_time.append(2)
                    update.append(
                        self.sql_update_2.format(
                            ought_amount=row['real_amount'] + row['discount_money'],
                            real_amount=row['real_amount'],
                            discount_amount=row['discount_money'],
                            id=self.mapping[row['id']]['new_id']
                        )
                    )
                    insert.append(
                        self.sql_insert_2.format(
                            ought_amount=self.mapping[row['id']]['new_ought'] - (row['real_amount'] + row['discount_money']),
                            id=self.mapping[row['id']]['new_id']
                        )
                    )

                if row['hang_up_bill_amount'] > 0 \
                        and (row['real_amount'] + row['discount_money']) > 0 \
                        and row['ought_amount'] >= (row['hang_up_bill_amount'] + row['real_amount'] + row['discount_money']):
                    many_time.append(3)
                    update.append(
                        self.sql_update_3.format(
                            ought_amount=row['real_amount'] + row['discount_money'],
                            real_amount=row['real_amount'],
                            discount_amount=row['discount_money'],
                            id=self.mapping[row['id']]['new_id']
                        )
                    )
                    insert.append(
                        self.sql_insert_3_1.format(
                            ought_amount=row['hang_up_bill_amount'],
                            id=self.mapping[row['id']]['new_id']
                        )
                    )
                    if row['ought_amount'] > (row['hang_up_bill_amount'] + row['real_amount'] + row['discount_money']):
                        insert.append(
                            self.sql_insert_3_2.format(
                                ought_amount=self.mapping[row['id']]['new_ought'] - (row['real_amount'] + row['discount_money'] + row['hang_up_bill_amount']),
                                id=self.mapping[row['id']]['new_id']
                            )
                        )

                if (row['real_amount'] + row['discount_money']) == 0 and row['ought_amount'] > row['hang_up_bill_amount'] > 0:
                    many_time.append(4)
                    update.append(
                        self.sql_update_4.format(
                            ought_amount=row['hang_up_bill_amount'],
                            id=self.mapping[row['id']]['new_id']
                        )
                    )
                    insert.append(
                        self.sql_insert_4.format(
                            ought_amount=self.mapping[row['id']]['new_ought'] - row['hang_up_bill_amount'],
                            id=self.mapping[row['id']]['new_id']
                        )
                    )

                if (row['real_amount'] + row['discount_money']) == 0 and row['ought_amount'] == row['hang_up_bill_amount'] > 0:
                    many_time.append(5)
                    update.append(
                        self.sql_update_5.format(
                            id=self.mapping[row['id']]['new_id']
                        )
                    )

                if row['hang_up_bill_amount'] == 0 and row['ought_amount'] < (row['hang_up_bill_amount'] + row['real_amount'] + row['discount_money']):
                    many_time.append(6)
                    update.append(
                        self.sql_update_6.format(
                            real_amount=row['ought_amount'],
                            id=self.mapping[row['id']]['new_id']
                        )
                    )

                if len(many_time) == 0:
                    self.no_match.append(row)
                elif len(many_time) == 1:
                    for u in update:
                        self.need_update.append(u)
                    for i in insert:
                        self.need_insert.append(i)
                else:
                    row['case'] = str(many_time)
                    self.match_many.append(row)
            else:
                self.not_in_new_bill.append(row)

        self.out_sql(path)

    @staticmethod
    def read_source_bill(source_bill_file):
        source_bill = list()
        with open(source_bill_file, 'r') as f:
            for row in f.readlines():
                row = row.replace('\n', '')
                arr = row.split(',')
                source_bill.append({
                    'id': arr[0],
                    'discount_money': Decimal(arr[1]),
                    'financial_income': Decimal(arr[2]),
                    'hang_up_bill_amount': Decimal(arr[3]),
                    'ought_amount': Decimal(arr[4]),
                    'real_amount': Decimal(arr[5]),
                })
        print('老的bill数量：', len(source_bill))
        return source_bill

    @staticmethod
    def read_mapping(mapping_file):
        mapping = dict()
        with open(mapping_file, 'r') as f:
            for row in f.readlines():
                row = row.replace('\n', '')
                arr = row.split(',')
                mapping[arr[0]] = {
                    'new_id': arr[1],
                    'new_ought': Decimal(arr[2])
                }  # key是老bill
        print('老的对应新的数量：', len(mapping))
        return mapping

    def out_sql(self, path):
        for root, dirs, files in os.walk(path):
            for name in files:
                if name.endswith(".jpg"):
                    os.remove(os.path.join(root, name))

        with open(path + '老的账单没有在新的里面' + '.txt', 'a') as f:
            for row in self.not_in_new_bill:
                f.write(str(row) + '\n')

        with open(path + '没有在任何case里面' + '.txt', 'a') as f:
            for row in self.no_match:
                f.write(str(row) + '\n')

        with open(path + '在多个case里面' + '.txt', 'a') as f:
            for row in self.match_many:
                f.write(str(row) + '\n')

        with open(path + '最终需要更新的数据' + '.sql', 'a') as f:
            for row in self.need_update:
                f.write(row + '\n')

        with open(path + '最终需要插入的数据' + '.sql', 'a') as f:
            for row in self.need_insert:
                f.write(row + '\n')


if __name__ == '__main__':
    wb = Wb('file/source_bill.txt', 'file/mapping.txt')
    wb.handle('file_out/')
