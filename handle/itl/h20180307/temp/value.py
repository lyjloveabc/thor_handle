import requests

response = requests.get(self.base_url + self.url.format(appid=app_id, sd=sd, ed=ed, limit=self.limit, os=os), cookies=self.cookies)

