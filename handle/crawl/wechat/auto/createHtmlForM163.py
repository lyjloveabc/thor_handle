"""
自动创建html代码
"""
from utils.constant.constant import Constant


class CreateHtmlForM163:
    __BASE_PATH = 'file/'

    def __init__(self):
        self.html_subscribed = """
                                <p style="text-align: left;">
                                    <strong><span style="font-size: 16px; color: rgb(255, 0, 0);">{index}、{name}</span></strong><br/>
                                </p>
                                <p style="text-align: left;">
                                    <span style="font-size: 14px;">收藏数：{count}</span>
                                </p>
                                <p style="text-align: left;">
                                    <span style="font-size: 14px;">标签： &nbsp; &nbsp;{tags}</span>
                                </p>
                                <p style="text-align: left;">
                                    <span style="font-size: 14px;">创建者：{creator_name}</span>
                                </p>
                                <p style="font-size:14px;color:rgb(66,66,66);margin: 5px 0 0;">
                                    <br/>
                                </p>
                                """
        self.html_share = """
                                <p style="text-align: left;">
                                    <strong><span style="font-size: 16px; color: rgb(255, 0, 0);">{index}、{name}</span></strong><br/>
                                </p>
                                <p style="text-align: left;">
                                    <span style="font-size: 14px;">分享数：{count}</span>
                                </p>
                                <p style="text-align: left;">
                                    <span style="font-size: 14px;">标签： &nbsp; &nbsp;{tags}</span>
                                </p>
                                <p style="text-align: left;">
                                    <span style="font-size: 14px;">创建者：{creator_name}</span>
                                </p>
                                <p style="font-size:14px;color:rgb(66,66,66);margin: 5px 0 0;">
                                    <br/>
                                </p>
                                """

        self.html_play = """
                                <p style="text-align: left;">
                                    <strong><span style="font-size: 16px; color: rgb(255, 0, 0);">{index}、{name}</span></strong><br/>
                                </p>
                                <p style="text-align: left;">
                                    <span style="font-size: 14px;">收听数：{count}</span>
                                </p>
                                <p style="text-align: left;">
                                    <span style="font-size: 14px;">标签： &nbsp; &nbsp;{tags}</span>
                                </p>
                                <p style="text-align: left;">
                                    <span style="font-size: 14px;">创建者：{creator_name}</span>
                                </p>
                                <p style="font-size:14px;color:rgb(66,66,66);margin: 5px 0 0;">
                                    <br/>
                                </p>
                                """

        self.html_comment = """
                                <p style="text-align: left;">
                                    <strong><span style="font-size: 16px; color: rgb(255, 0, 0);">{index}、{name}</span></strong><br/>
                                </p>
                                <p style="text-align: left;">
                                    <span style="font-size: 14px;">评论数：{count}</span>
                                </p>
                                <p style="text-align: left;">
                                    <span style="font-size: 14px;">标签： &nbsp; &nbsp;{tags}</span>
                                </p>
                                <p style="text-align: left;">
                                    <span style="font-size: 14px;">创建者：{creator_name}</span>
                                </p>
                                <p style="font-size:14px;color:rgb(66,66,66);margin: 5px 0 0;">
                                    <br/>
                                </p>
                                """

    def handle(self):
        CreateHtmlForM163.out_file('被收藏top10.txt', self.html_subscribed)
        CreateHtmlForM163.out_file('被分享top10.txt', self.html_share)
        CreateHtmlForM163.out_file('被收听top10.txt', self.html_play)
        CreateHtmlForM163.out_file('被评论数top10.txt', self.html_comment)

    @staticmethod
    def out_file(read_file_name, base_html):
        with open(CreateHtmlForM163.__BASE_PATH + 'out' + read_file_name, 'w') as out:
            with open(CreateHtmlForM163.__BASE_PATH + read_file_name, 'r') as f:
                index = 1
                for line in f.readlines():
                    data_split = line[:-1].split(Constant.SEMICOLON_SEP)
                    name = data_split[0]
                    count = data_split[1]
                    tags = data_split[2]
                    creator_name = data_split[3]
                    out.write(base_html.format(index=index, name=name, count=count,
                                               tags=tags, creator_name=creator_name))
                    index += 1


if __name__ == '__main__':
    CreateHtmlForM163().handle()
