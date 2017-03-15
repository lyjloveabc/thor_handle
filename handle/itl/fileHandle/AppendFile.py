"""
多个文件追加
"""

class AppendFile(object):
    __BASE_PATH = 'file/'

    def __init__(self):
        pass

    @staticmethod
    def handle():

        with open('file/中国轴承行业网_VIP才可见的文章_20170313.txt', 'r') as f:
            for line in f.readlines():
                line_split = line[:-1].split(': ')
                try:
                    pdfkit.from_url(line_split[1], 'out/' + line_split[0] + '.pdf', options=options)
                except IOError:
                    print('UnicodeDecodeError:', line_split)


if __name__ == '__main__':
    handle = AppendFile()
    handle.handle()
