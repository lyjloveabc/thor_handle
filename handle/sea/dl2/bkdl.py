# 处理日期
import os


class Bkdl:
    @staticmethod
    def handle(path='data_hy', res_file='res_hy'):
        for root, dirs, files in os.walk(path):
            # root 表示当前正在访问的文件夹路径
            # dirs 表示该文件夹下的子目录名list
            # files 表示该文件夹下的文件list

            # 一个文件一个对象
            all_data = list()

            # 遍历文件
            for file in files:
                with open(os.path.join(root, file), 'r') as f:
                    file_data = dict()
                    index = 1
                    all_row = f.readlines()
                    for row in all_row[2: len(all_row) - 1]:
                        attrs = row.replace('\n', '').split('	')
                        hy_name = attrs[1]
                        file_data[hy_name] = index
                        index += 1
                    all_data.append(file_data)

            res = list()
            for row in all_data[len(all_data) - 1]:
                row_data = list()
                row_data.append(row)
                for temp_data in all_data[::-1]:
                    row_data.append(temp_data[row])
                res.append(row_data)

            with open('res/{}.txt'.format(res_file), 'w') as f:
                for row in res:
                    f.write(' '.join(str(i) for i in row))
                    f.write('\n')


if __name__ == '__main__':
    Bkdl.handle('data_hy', 'res_hy')
    Bkdl.handle('data_gn', 'res_gn')
