import datetime
import json
import requests


class Detail:
    def __init__(self):
        self.today = datetime.datetime.now()
        self.file_date_str = '_' + self.today.strftime('%Y%m%d')

        self.url = 'https://www.wenjuan.in/s/UjayMfe/'

    def handle(self):
        url_2 = 'https://www.wenjuan.in/s/project_mobile_authentication'
        response = requests.get(self.url)
        response = requests.get(self.url)
        print(response.text)
        # json_data = json.loads(response.text)
        # print(json_data)


if __name__ == '__main__':
    tjMd = Detail()
    tjMd.handle()

# http://127.0.0.1:8001/work/batchWorkDetail.do?app=GJ&client=iPhone&version=1.6.6&outerType=STAFF&token=77f56c02a13b828aa80769cf495cf0fc&userId=35&zoneId=1&detailType=POST_THING&detailIdStr=2360145,2345986,2345989,2345480,2345481,2345482,2345483,2345484,2345485,2345486,2341647,2345487,2341648,2345488,2341649,2345489,2341650,2345490,2345491,2345492


# http://127.0.0.1:8001/work/workDetail.do?app=GJ&client=iPhone&version=1.6.6&outerType=STAFF&token=77f56c02a13b828aa80769cf495cf0fc&userId=35&zoneId=1&detailType=COMPALIN&detailId=1630
