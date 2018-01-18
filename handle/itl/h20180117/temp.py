import json
import random

import requests

from utils.constant.constant import Constant

response = requests.get("https://danjuanapp.com/djapi/index_eva/dj", headers={'User-Agent': random.choice(Constant.UA_GROUP)})

with open('fund_20180117.json', 'w') as f:
    f.write(str(response.text))
