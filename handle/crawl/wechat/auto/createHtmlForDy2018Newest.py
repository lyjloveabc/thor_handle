"""
自动创建html代码
"""
from utils.constant.constant import Constant


class CreateHtmlForDy2018Newest:
    __BASE_PATH = 'file/'

    def __init__(self):
        self.html = """
        <section class="wx96Diy" data-source="bj.96weixin.com">
    <section style="padding: 5px;box-shadow: rgb(198,198,199) 5px 5px 3px;background-color: rgb(250, 250, 250);margin: 20px 10px 10px;">
        <section style="text-align:left;margin-left:20px;width: auto;margin-top: -15px;">
            <section style="border-radius: 0.2em 1.1em;box-shadow: rgb(165, 165, 165) 4px 4px 2px;color: rgb(255, 255, 255);padding: 4px 10px;display: inline-block;font-size: 20px;background-color: rgb(173, 172, 159);" class="96wx-bgc">
                <strong>{index}</strong>
            </section>
            <section style="padding:5px 10px 5px;">
                <p>
                    <span style="color: rgb(255, 0, 0);">{name}</span>
                </p>
                <p>
                点击量：{count}
                </p>
            </section>
        </section>
    </section>
</section>
                                """

    def handle(self):
        CreateHtmlForDy2018Newest.out_file('电影天堂点击量TOP30.txt', self.html)

    @staticmethod
    def out_file(read_file_name, base_html):
        with open(CreateHtmlForDy2018Newest.__BASE_PATH + 'out' + read_file_name, 'w') as out:
            with open(CreateHtmlForDy2018Newest.__BASE_PATH + read_file_name, 'r') as f:
                index = 1
                for line in f.readlines():
                    data_split = line[:-1].split(Constant.DEFAULT_SEP)
                    name = data_split[0]
                    count = data_split[1]
                    out.write(base_html.format(index=index, name=name, count=count))
                    index += 1


if __name__ == '__main__':
    CreateHtmlForDy2018Newest().handle()

# select name, click_count from dy2018_newest
# where name != ''
# order by click_count desc
# limit 30;
