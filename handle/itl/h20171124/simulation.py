import logging
import requests
from datetime import datetime

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='getQQMsg.py.log',
                    filemode='a')


class Simulation:
    def __init__(self):
        logging.info('============> ' + ' init ' + str(datetime.now()))

    def handle(self):
        headers = {
            'Accept': '*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': '331',
            'content-type': 'application/x-www-form-urlencoded',
            'Cookie': 'pac_uid=1_546223592; tvfe_boss_uuid=6530508c4b2e6648; pgv_pvi=5384152064; RK=nMOCbf+7c/; mobileUV=1_15ba337c809_8b7a9; sd_userid=50741498985632643; sd_cookie_crttime=1498985632643; LW_sid=C175P0x412h6K815B0x2J320K2; LW_uid=o125V0m4U2S668n5u0z2t3L0D6; eas_sid=u1p5y0d4e286D8I550H2U312t0; pgv_info=ssid=s4839464464; pgv_pvid=2316728870; o_cookie=546223592; pgv_si=s3600361472; enc_uin=mvh2MRs561oJUYYAmdtrgw; ptisp=ctc; ptcz=363a0364abd2d8da5de25e61fd3a0cfa0aaed4315c067b5c2f5e3636e5468d10; uin=o0546223592; skey=@x2U00BaS4; pt2gguin=o0546223592; p_uin=o0546223592; pt4_token=WHT6bygrk69LHWiFFFxBBfHEdYW59C2qgzkLJWkgeeo_; p_skey=bD-xXwyHM-XshcSUnOeawlcA9TUugjf9FgdB7TOyHp0_',
            'Host': 'd1.web2.qq.com',
            'Origin': 'http://d1.web2.qq.com',
            'Referer': 'http://d1.web2.qq.com/proxy.html?v=20151105001&callback=1&id=2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        }

        json = {
            'r': '{"ptwebqq":"","clientid":53999199,"psessionid":"8368046764001d636f6e6e7365727665725f77656271714031302e3133332e34312e383400001ad00000066b026e040015808a206d0000000a406172314338344a69526d0000002859185d94e66218548d1ecb1a12513c86126b3afb97a3c2955b1070324790733ddb059ab166de6857","key":""}'
        }
        while True:
            response = requests.post('http://d1.web2.qq.com/channel/poll2', headers=headers, json=json)
            print(response.text)


if __name__ == '__main__':
    acl = Simulation()
    acl.handle()
