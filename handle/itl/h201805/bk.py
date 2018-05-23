import datetime
import json
import requests


class Bk:
    def __init__(self):
        self.today = datetime.datetime.now()
        self.file_date_str = '_' + self.today.strftime('%Y%m%d')

        self.headers = {
            # 'Page-Schema': 'CommunityDetailActivity',
            'Page-Schema': 'community%2Flist',
            'Referer': 'community%2Flist%3Flimit_offset%3D0%26limit_count%3D20%26city_id%3D330100',
            'Cookie': 'lianjia_udid=867180036615534;lianjia_uuid=9bf690e3-99d0-443a-8ae6-aa643ed278a8',
            'Lianjia-City-Id': '330100',
            'extension': 'lj_android_id=366d21f2e86a3d16&lj_imei=867180036615534&lj_device_id_android=867180036615534&mac_id=A8:0C:63:51:1E:6D',
            'User-Agent': 'Beike1.1.5;HONOR STF-AL10; Android 8.0.0',
            'Lianjia-Channel': 'Android_ke_huawei',
            'Lianjia-Device-Id': '867180036615534',
            'Lianjia-Version': '1.1.5',
            'Authorization': 'MjAxODAxMTFfYW5kcm9pZDpiZWY4ZDU1YzkyNTk5YjExOTUzMzNhNjNhOWY4NjA1NWJiZGE2NmYw',
            'Lianjia-Im-Version': '2.12.0',
            'Host': 'app.api.ke.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'If-Modified-Since': 'Mon, 21 May 2018 15:17:00 GMT',
            'Accept': '*/*',
        }

        self.list_url = 'https://app.api.ke.com/house/community/search?limit_offset={limit_offset}&limit_count=20&city_id=330100'
        self.detail_url = 'https://app.api.ke.com/house/community/detailpart1?community_id={community_id}'

    def handle(self):
        self.request_list(0)

        # response = requests.get(self.detail_url.format(community_id=1811628648345706), headers=self.headers)
        # json_data = json.loads(response.text)
        # print(json_data)

    def request_list(self, limit_offset):
        list_response = requests.get(self.list_url.format(limit_offset=limit_offset), headers=self.headers)
        list_data = json.loads(list_response.text)

        print(list_data)

        zone_list_data = list_data['data']['list']

        if len(zone_list_data) > 0:
            for row in zone_list_data:
                print(row['community_id'])
        has_more_data = list_data['data']['has_more_data']
        if has_more_data == 1:
            limit_offset += 20
            self.request_list(limit_offset)


if __name__ == '__main__':
    tjMd = Bk()
    tjMd.handle()
