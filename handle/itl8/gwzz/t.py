sql = 'UPDATE itl_perf_job_explain SET explain_url = "{eu}" WHERE job_title_id = {ji};'

insert = 'INSERT INTO itl_perf_job_explain(id, gmt_create, gmt_modified, job_title_id, explain_url) VALUES ({id}, now(), now(), {ji}, "{eu}");'

with open('d.txt', 'r') as f:
    for row in f.readlines():
        row = row.replace('\n', '')
        line = row.split(',')
        print(sql.format(eu=line[1], ji=line[0]))

ii = 10

new_data = "14,http://itianluo-apiupload.oss-cn-hangzhou.aliyuncs.com/itl/p/65f8ca14-da54-4c3c-af57-420398b30f03.jpg".split(",")
print(insert.format(id=ii, ji=new_data[0], eu=new_data[1]))
