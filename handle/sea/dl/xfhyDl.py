# 处理日期
import time


class XfhyDl:
    @staticmethod
    def handle(day=time.strftime('%Y%m%d', time.localtime(time.time()))):
        # 读取所有数据
        total = dict()  # 分组数据
        total_every = list()  # 所有数据
        with open('data/沪深Ａ股{}.txt'.format(day), 'r') as f:
            all_row = f.readlines()
            for row in all_row[2: len(all_row) - 1]:
                row = row.replace('\n', '')
                value_array = row.split('	')
                xfhy = value_array[9]

                total_every.append(xfhy)

                if xfhy in total:
                    total[xfhy] = total[xfhy] + 1
                else:
                    total[xfhy] = 1
        print('total: ', total)

        # 读取动量榜前排的数据
        part = dict()
        for row in total_every[0: round(len(total_every) * 0.13)]:
            row = row.replace('\n', '')

            if row in part:
                part[row] = part[row] + 1
            else:
                part[row] = 1
        print('part: ', part)

        # 计算板块的动量分值
        res = dict()
        for k, v in total.items():
            value = {
                'rate': 0,
                'score': 0,
            }
            if k in part:
                value = {
                    'rate': round(100 * part[k] / total[k], 4),
                    'score': round(part[k] * part[k] / total[k], 4),
                }
            res[k] = value
        print('res: ', res)

        # 输出结果
        with open('res/res{}.txt'.format(day), 'w', encoding="UTF-8-sig") as f:
            f.truncate()
            # f.write('{0} {1} {2}\n'.format('细分行业', '动量分值', '个数占比'))
            for row in sorted(res.items(), key=lambda kv: (kv[1]['score'], kv[0]), reverse=True):
                f.write('{0} {1} {2}\n'.format(row[0], row[1]['score'], row[1]['rate']))


if __name__ == '__main__':
    XfhyDl.handle()
