import re

__AUTHOR = 'thor'


class DataMatch(object):
    __BASE_PATH = 'file/'

    def __init__(self):
        pass

    def handle(self):
        zfb = list()
        with open(DataMatch.__BASE_PATH + 'zfb.txt', 'r') as f:
            for line in f.readlines():
                zfb.append(line[:-1])
        my = list()
        with open(DataMatch.__BASE_PATH + 'my.txt', 'r') as f:
            for line in f.readlines():
                my.append(line[:-1])

        for m in my:
            if m not in zfb:
                print(m)

        print("      ")

        for z in zfb:
            if z not in my:
                print(z)


if __name__ == '__main__':
    handle = DataMatch()
    handle.handle()
