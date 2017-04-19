"""
自动创建html代码
"""
from utils.constant.constant import Constant


class CreateHtmlForM163Folk:
    __BASE_PATH = 'file/'

    def __init__(self):
        self.html = """
                                <p style="text-align: left;">
                                    <strong><span style="font-size: 16px; color: rgb(255, 0, 0);">{index}、{name}</span></strong><br/>
                                </p>
                                <p style="text-align: left;">
                                    <span style="font-size: 14px;">被收录到：{count} 张歌单</span>
                                </p>
                                <p style="text-align: left;">
                                    <span style="font-size: 14px;">歌手： &nbsp; &nbsp;{tags}</span>
                                </p>
                                <p style="font-size:14px;color:rgb(66,66,66);margin: 5px 0 0;">
                                    <br/>
                                </p>
                                """

    def handle(self):
        CreateHtmlForM163Folk.out_file('被收录到N张歌单TOP30.txt', self.html)

    @staticmethod
    def out_file(read_file_name, base_html):
        with open(CreateHtmlForM163Folk.__BASE_PATH + 'out' + read_file_name, 'w') as out:
            with open(CreateHtmlForM163Folk.__BASE_PATH + read_file_name, 'r') as f:
                index = 1
                for line in f.readlines():
                    data_split = line[:-1].split(Constant.DEFAULT_SEP)
                    name = data_split[0]
                    count = data_split[1]
                    artist_name = data_split[2]
                    out.write(base_html.format(index=index, name=name, count=count,
                                               tags=artist_name))
                    index += 1


if __name__ == '__main__':
    CreateHtmlForM163Folk().handle()

# select m163_song.`name`, count(1) as c, m163_song.first_artist_name
# from m163_playlist_x_song
# left join m163_song on m163_song.m163_id = m163_playlist_x_song.m163_song_id
# group by m163_song_id
# order by c desc limit 30;
