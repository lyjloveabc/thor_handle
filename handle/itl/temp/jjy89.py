import json
import xml.dom.minidom

sql = "UPDATE subscription_enter SET detail = '{new_detail}' WHERE id = '{id}';"

data_74 = dict()
collection_74 = xml.dom.minidom.parse('74.xml').documentElement
records_74 = collection_74.getElementsByTagName("RECORD")

for record in records_74:
    record_id = record.getElementsByTagName('id')[0].childNodes[0].data
    house_info_id = record.getElementsByTagName('house_info_id')[0].childNodes[0].data
    detail = record.getElementsByTagName('detail')[0].childNodes[0].data
    data_74[house_info_id] = json.loads(detail)

collection_75 = xml.dom.minidom.parse('75.xml').documentElement
records_75 = collection_75.getElementsByTagName("RECORD")

print(len(records_75))

for record in records_75:
    record_id = record.getElementsByTagName('id')[0].childNodes[0].data
    house_info_id = record.getElementsByTagName('house_info_id')[0].childNodes[0].data
    detail = record.getElementsByTagName('detail')[0].childNodes[0].data

    detail_75 = json.loads(detail)

    # print(detail_75['current_num'])
    # print(data_74[house_info_id]['current_num'])
    # print(detail_75['current_num'] - data_74[house_info_id]['current_num'])
    new_detail = {
        "last_num": data_74[house_info_id]['current_num'],
        "lastdate": data_74[house_info_id]['currentdate'],
        "current_num": detail_75['current_num'],
        "currentdate": "2017-09-29",
        "actualUse": detail_75['current_num'] - data_74[house_info_id]['current_num'],
        "unitPrice": detail_75['unitPrice']
    }

    print(sql.format(new_detail=json.dumps(new_detail), id=record_id))
