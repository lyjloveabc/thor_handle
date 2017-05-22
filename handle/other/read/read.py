"""

"""
from utils.constant.constant import Constant


class Read:
    def __init__(self):
        pass

    def handle(self):
        with open(Constant.BASE_PATH + 'read.txt', 'r') as f:
            for line in f.readlines():
                line_split = line[:-1].split(',')
                print(line_split[0] +
                      '("' + line_split[0] + '", "' + line_split[1] + '"),')


if __name__ == '__main__':
    obj = Read()
    obj.handle()
