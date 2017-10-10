from utils.file.excel.readUtil import ReadUtil


class Hb:
    def handle(self):
        sql = 'INSERT INTO bill(zone_id, house_info_id, title, product_type_id, product_type_code, product_id,' \
              'sub_enter_id, billing_period, ought_amount, real_amount, gmt_start, gmt_end, gmt_create,' \
              'gmt_modify, remark, status, is_checked, financial_income)' \
              'VALUES("{zone_id}", "{house_info_id}", "{title}", "{product_type_id}", "{product_type_code}", "{product_id}",' \
              'NULL , "{billing_period}", "{ought_amount}", "{real_amount}", "{gmt_start}",' \
              '"{gmt_end}", now(), now(), "{remark}", "{status}", "{is_checked}", "{financial_income}");'
        field_index = {
            'house_info': 0,
            'period': 5,
            'period_name': 6,
            'ought_amount': 7
        }

        data = ReadUtil.read_file('田螺财务收费系统生成账单核对20171009.xlsx', field_index=field_index)
        house_W = dict()

        with open('houW.txt', 'r') as f:
            for line in f.readlines():
                line_split = line[:-1].split(',')
                house_W[line_split[1]] = line_split[0]

        for row in data:
            p_s = str(row['period']).split('月-')
            ps_s = p_s[0].split('年')
            print(sql.format(zone_id=24, house_info_id=house_W[row['house_info']], title=row['period_name'],
                             product_type_id=7, product_type_code='propertyFee', product_id=24, billing_period=row['period_name'],
                             ought_amount='%.2f' % float(row['ought_amount']), real_amount=0.00, gmt_start=ps_s[0] + '-' + ps_s[1] + '-01',
                             gmt_end=ps_s[0] + '-' + p_s[1][:-1] + '-01', remark='手动生成的历史遗留数据', status='NO_PAY', is_checked=1,
                             financial_income='%.2f' % float(row['ought_amount'])
                             )
                  )


if __name__ == '__main__':
    hb = Hb()
    hb.handle()
