import random
import datetime

person = [
    "是未知浪",
    "黄家驹",
    "谎言",
    "旧城的人",
    "困住了的人",
    "张老师",
    "张学友",
    "刘德华",
    "天空之城",
    "脸",
    "无情",
    "无言",
    "我的天",
    "龙人",
]

content = [
    "中国银行、工商银行、建设银行",
    "各位运维同行朋友们，大家好，非常高兴",
    "开始之前，本人首先做一下自我介绍",
    "阿里、腾讯、百度、京东、网易、新浪、搜狐、大众点评、饿了么",
    "大厅灯坏了也没人修理啊",
    "这个物业太差了啊",
    "举报南门岗保安在嗑瓜子",
    "天气不太好啊",
    "风吹草低见牛羊",
    "一幢大门坏了",
    "我们物业什么时候到期啊",
    "呵呵，这个东西太傻了啊",
    "我们的物业太差了，能不能改选啊",
    "物业怎么换届的",
    "我们的物业还行",
    "这个物业是神经病啊",
    "赶紧换物业",
    "抗议抗议",
]

time = [
    "080000",
    "090201",
    "100300",
    "110000",
    "120000",
    "130000",
]


def aa(gr):
    start = '2017-12-24'
    end = '2017-12-26'

    datestart = datetime.datetime.strptime(start, '%Y-%m-%d')
    dateend = datetime.datetime.strptime(end, '%Y-%m-%d')
    while datestart < dateend:
        date_str = datestart.strftime('%Y%m%d')
        with open("file/" + gr + "_" + date_str + ".data", "a") as f:
            for index in range(1, 2001):
                p = person[random.randint(0, len(person) - 1)]
                c = content[random.randint(0, len(content) - 1)]
                t = date_str + time[random.randint(0, len(time) - 1)]

                f.write("{person}|{content}|{time}|{group}".format(person=p, content=c, time=t, group=gr))
                f.write("\n")
        datestart += datetime.timedelta(days=1)


def bb(gr):
    start = '2017-11-19'
    end = '2017-12-26'

    datestart = datetime.datetime.strptime(start, '%Y-%m-%d')
    dateend = datetime.datetime.strptime(end, '%Y-%m-%d')
    with open("file/g15_today_messages.data", "a") as f:
        while datestart < dateend:
            date_str = datestart.strftime('%Y%m%d')
            for index in range(1, 2001):
                p = person[random.randint(0, len(person) - 1)]
                c = content[random.randint(0, len(content) - 1)]
                t = date_str + time[random.randint(0, len(time) - 1)]

                f.write("{person}|{content}|{time}|{group}|{day}".format(person=p, content=c, time=t, group=gr, day=date_str))
                f.write("\n")
            datestart += datetime.timedelta(days=1)


for index in range(1, 6):
    bb(str(index))
