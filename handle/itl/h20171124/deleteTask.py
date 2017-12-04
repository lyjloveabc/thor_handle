# delete from itl_zone_task where zone_id in (SELECT id FROM zones WHERE name IN ('恒生电商产业园','湖塘悦色','正淘易谷创新园','星河上城','盛世龙城','新世纪广场','泗水古城','阳光幸福里','阳光嘉园','桐汭首府','龙湖国际','晴彩巴厘','绿岸科创园','海创大厦','铭鹤花园','柳浪新苑','南湖明筑苑','野风启城'))
# delete FROM `itl_user_task` WHERE 1 AND `zone_task_id` not in (select id from itl_zone_task)

class DeleteTask:
    def __init__(self):
        pass

    def handle(self):
        pass


if __name__ == '__main__':
    zones = list()
    with open('deleteTask.txt', 'r') as f:
        for line in f.readlines():
            zones.append(line[:-1])

    sql = 'SELECT id FROM zones WHERE name IN ('
    for z in zones:
        sql += '\'' + z + '\','

    sql = sql[:-1] + ')'
    print(sql)

    obj = DeleteTask()
    obj.handle()
