# 处理日期
import os


class Bkdl:
    @staticmethod
    def handle(path='data', out='res/res.txt'):
        for root, dirs, files in os.walk(path):
            # root 表示当前正在访问的文件夹路径
            # dirs 表示该文件夹下的子目录名list
            # files 表示该文件夹下的文件list

            # 一个文件一个对象
            all_data = list()

            # 遍历文件，拿到每一天的数据
            for file in files:
                all_data.append(Bkdl.day_dl(os.path.join(root, file)))

            res_data = list()
            last_day_data = all_data[len(all_data) - 1]
            for row in sorted(last_day_data.items(), key=lambda kv: (kv[1]['score'], kv[0]), reverse=True):
                row_data = list()
                row_data.append(row[0])
                for temp_data in all_data[::-1]:
                    row_data.append(temp_data[row[0]]['rank'])
                res_data.append(row_data)

            with open(out, 'w', encoding='utf-8-sig') as f:
                for row in res_data:
                    f.write(' '.join(str(i) for i in row))
                    f.write('\n')

    @staticmethod
    def day_dl(file):
        """
        计算某一天的各个板块的动量分值和占比
        :param file:
        :return: 字典，key是行业名称，value是占比和分值
        """
        # 读取所有数据
        all_gp = list()  # 所有股票数据
        total_group = dict()  # 细分行业分组数据
        with open(file, 'r') as f:
            rows = f.readlines()
            for row in rows[2: len(rows) - 1]:
                attrs = row.replace('\n', '').split('	')
                xfhy = attrs[9]

                if xfhy == '':
                    continue

                all_gp.append(xfhy)

                if xfhy in total_group:
                    total_group[xfhy] = total_group[xfhy] + 1
                else:
                    total_group[xfhy] = 1
        print(file, 'total_group:', total_group)

        # 读取动量榜前排的数据
        part_group = dict()
        for row in all_gp[0: round(len(all_gp) * 0.13)]:
            if row in part_group:
                part_group[row] = part_group[row] + 1
            else:
                part_group[row] = 1
        print(file, 'part_group:', part_group)

        # 计算板块的动量分值
        res = dict()
        res_temp = dict()
        for k, v in total_group.items():
            value = {
                'rate': 0,
                'score': 0,
            }
            if k in part_group:
                value = {
                    'rate': round(100 * part_group[k] / total_group[k], 4),
                    'score': round(part_group[k] * part_group[k] / total_group[k], 4),
                }
            res_temp[k] = value
        index = 1
        for row in sorted(res_temp.items(), key=lambda kv: (kv[1]['score'], kv[0]), reverse=True):
            res[row[0]] = {
                'score': row[1]['score'],
                'rate': row[1]['rate'],
                'rank': index
            }
            index += 1
        print(file, 'day_dl_res: ', res)

        return res


if __name__ == '__main__':
    Bkdl.handle()
