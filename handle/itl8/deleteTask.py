from utils.file.excel.readUtil import ReadUtil

delete_sql = 'DELETE FROM itl_zone_task WHERE zone_id = "{zone_id}";'

de = ReadUtil.read_file('任务库涉及到的小区_20181016.xls', {'id': 0, 'de': 5})

zone_ids = list()
for row in de:
    if row['de'] == '√':
        zone_ids.append(str(int(float(row['id']))))

print(",".join(zone_ids))
