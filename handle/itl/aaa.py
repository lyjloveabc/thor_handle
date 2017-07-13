with open('aa.txt', 'r') as f:
    for row in f.readlines():
        print("INSERT INTO itl_user_task (zone_task_id, user_id) VALUES (" + str(row[:-1]) + ", 922);")
