"""
添加AddAliAppId
"""
import json
import re
import xml.dom.minidom

from utils.ExcelReadUtil import ExcelReadUtil

__AUTHOR = 'thor'


class AddAliAppId(object):
    __BASE_PATH = 'file/'

    def __init__(self):
        pass

    def handle(self):
        with open(AddAliAppId.__BASE_PATH + 'aliAppId.json') as json_file:
            data = json.load(json_file)
            for item in data['aliAppId']:
                print('insert into ali_app_id (gmt_create, gmt_modify, app_id, app_name, partner, seller_id, ali_public_key, '
                      'my_public_key, my_private_key, security_verify_key, zone_id) values '
                      '(now(), now(), \'{app_id}\', \'{app_name}\', \'{partner}\', \'{seller_id}\', \'{ali_public_key}\', '
                      '\'{my_public_key}\', \'{my_private_key}\', \'{security_verify_key}\', \'{zone_id}\');'
                      .format(app_id=item['appId'], app_name=item['appName'], partner=item['partner'], seller_id=item['sellerId'],
                              ali_public_key=item['aliPublicKey'], my_private_key=item['myPrivateKey'],
                              my_public_key=item['myPublicKey'], security_verify_key=item['securityVerifyKey'],
                              zone_id=item['zoneId']))


if __name__ == '__main__':
    handle = AddAliAppId()
    handle.handle()
