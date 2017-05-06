"""
账号有特殊字符
"""
import re


class ErrorMobile:
    __BASE_PATH = 'file/'

    def __init__(self):
        pass

    def handle(self):
        old_user_group = self.get_old_user_group()

        keys = old_user_group.keys()
        for key in keys:
            flag = re.match(r'\d+', str(old_user_group[key]['mobile']))
            if flag is None:
                print(old_user_group[key]['mobile'])

    @staticmethod
    def get_old_user_group():
        old_user_group = dict()
        with open(ErrorMobile.__BASE_PATH + 'oldUser.txt', 'r') as f:
            for line in f.readlines():
                temp = line[:-1].split(';')
                old_user = {'id': temp[0],
                            'cid': temp[1],
                            'type': temp[2],
                            'manager': temp[3],
                            'zone_id': temp[4],
                            'name': temp[5],
                            'job': temp[6],
                            'sex': temp[7],
                            'mobile': temp[8],
                            'emergency_mobile': temp[9],
                            'emergency_name': temp[10],
                            'password': temp[11],
                            'avtar': temp[12],
                            'address': temp[13],
                            'Idcard': temp[14],
                            'status': temp[15],
                            'is_employ': temp[16],
                            'work_status': temp[17],
                            'sort_num': temp[18],
                            'app_version': temp[19],
                            'device_type': temp[20],
                            'score': temp[21],
                            'level': temp[22],
                            'on_job': temp[23],
                            'in_list': temp[24],
                            'job_post_id': temp[25],
                            'jpid': temp[26],
                            'has_kpi': temp[27],
                            'switch': temp[28],
                            'role': temp[29],
                            'baas': temp[30],
                            'day_time': temp[31],
                            'day_time2': temp[32]
                            }
                if old_user['mobile'] == '':
                    print('没有mobile: ', old_user['id'])
                else:
                    old_user_group[old_user['mobile']] = old_user
        return old_user_group


if __name__ == '__main__':
    handle = ErrorMobile()
    handle.handle()
