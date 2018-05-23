import datetime
import json
import requests


class Work:
    def __init__(self):
        self.today = datetime.datetime.now()
        self.file_date_str = '_' + self.today.strftime('%Y%m%d')

        self.ENV_IP = '127.0.0.1:8001'
        # self.ENV_IP = 'prenewcloud.itianluo.cn'
        self.url = 'http://{ENV_IP}/work/workList.do?app=GJ&client=iPhone&version=1.6.6&outerType=STAFF&token=451feaccf02991c99462a76eb794b577&userId=1780' \
            .format(ENV_IP=self.ENV_IP)

    def handle(self):
        task = 'TASK'
        task_search_param = {
            'taskListFrom': 'MY_NEED_DO'
        }

        plan = 'PLAN'
        plan_search_param = {
            'exeCategoryIdStr': '2'
        }

        post_thing = 'POST_THING'
        post_thing_search_param = {
            'postThingListFrom': 'POST_CENTER',
            'launchEndTime': '2017-05-11',
            'content': 'Op',
            'returnVisitStatus': 'NEED_TO',
            'postThingStatus': '1',
            'returnVisitResult': 'HIGH',
            'followIdStr': '1750',
            'launchStartTime': '2016-05-11',
            'launchUserIdStr': '312',
            'isUrgent': '0',
        }

        complain = 'COMPLAIN'
        complain_search_param = {
            'complainListFrom': 'HIS_RECEIVED',
            'beComplainUserIdStr': '1750'
        }

        praise = 'PRAISE'
        praise_search_param = {
            'praiseListFrom': 'PRAISE_CENTER'
        }

        repair = 'REPAIR'
        repair_search_param = {
            'repairListFrom': 'REPAIR_CENTER',
            'repairType': 200,
        }

        rv = 'RETURN_VISIT'
        rv_search_param = {
            # 'returnVisitType': 'POST_THING'
            'returnVisitStatus': 'NEED_TO',
            # 'returnVisitType': 'POST_THING'
        }

        work_type = rv
        search_param = rv_search_param

        param = {
            # 'app': 'GJ',
            # 'client': 'iPhone',
            # 'version': '1.6.6',
            # 'outerType': 'STAFF',
            # 'token': '77f56c02a13b828aa80769cf495cf0fc',
            # 'userId': '35',

            'zoneId': '1',
            'pageNum': '1',
            'pageSize': '20',
            'workType': work_type,
            'workListSearch': json.dumps(search_param)
        }

        # headers = {'content-type': 'application/json'}
        headers = {}
        response = requests.post(self.url, headers=headers, data=param)
        json_data = json.loads(response.text)
        print(json_data)


if __name__ == '__main__':
    tjMd = Work()
    tjMd.handle()
