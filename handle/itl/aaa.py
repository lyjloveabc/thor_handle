# with open('aa.txt', 'r') as f:
#     for row in f.readlines():
#         print("INSERT INTO itl_user_task (zone_task_id, user_id) VALUES (" + str(row[:-1]) + ", 922);")

for row in range(45, 95):
    print("INSERT INTO itl_user_task(created_time, modified_time, zone_task_id, user_id) " \
          "VALUES(now(), now(), " + str(row) + ", 922); ")
