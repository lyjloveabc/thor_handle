import os
import logging
import smtplib

from datetime import datetime
from email.mime.text import MIMEText

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='ClearOldLog.log',
                    filemode='a')


class ClearOldLog:
    __DAY = 10  # 日期阈值
    __MAIL_TO = ["546223592@qq.com", 'luoyanjie@itianluo.cn', 'huangzhen@itianluo.cn']  # 目标邮箱列表

    def __init__(self):
        self.log = list()
        logging.info('============> init ' + str(datetime.now()))
        self.log.append('============> init ' + str(datetime.now()))

    def handle(self, base_path, sub_paths):
        if base_path == '' or sub_paths == '':
            logging.info('No path data!')
            self.log.append('No path data!')
            return

        delete_file = set()

        for sub_path in sub_paths:
            for dir_path, dir_names, file_names in os.walk(base_path + sub_path):
                for file_name in file_names:
                    if ClearOldLog.need_delete(file_name):
                        delete_file.add(os.path.join(dir_path, file_name))

        self.to_delete(delete_file)

        logging.info('End. \n')
        self.log.append('End. \n')

        Email.send_mail('定时清空日志', "\n".join(self.log), ClearOldLog.__MAIL_TO)

    @staticmethod
    def need_delete(file_name):
        result = False
        file_name_split = file_name.split('.')

        if len(file_name_split) == 3 and file_name_split[1] is not None and file_name_split[1] != '':
            log_time = datetime.strptime(file_name_split[1] + ' 23:59:59.999999', '%Y-%m-%d %H:%M:%S.%f')
            if (datetime.now() - log_time).days > ClearOldLog.__DAY:
                result = True

        return result

    def to_delete(self, delete_file):
        if len(delete_file) <= 0:
            logging.info('^.^ no data to delete ^.^')
            self.log.append('^.^ no data to delete ^.^')

        for file in delete_file:
            if os.path.isfile(file):
                os.remove(file)
                logging.info('> delete: ' + file)
                self.log.append('> delete: ' + file)


class Email:
    __HOST = "smtp.163.com"  # SMTP 服务器主机
    __USER = "luoyanjiewade@163.com"
    __PWD = "zucc416lyj"  # 163邮箱smtp生成的密码

    @staticmethod
    def send_mail(sub, content, to_list, product='netease'):
        if product == 'netease':
            Email.netease(sub, content, to_list)

    @staticmethod
    def netease(sub, content, to_list):
        """
        网易邮箱发送邮件
        :param sub: 主题
        :param content: 内容
        :param to_list: 发送目标
        :return: 发送成功返回True
        """
        me = "Thor" + "<" + Email.__USER + ">"

        msg = MIMEText(content, _subtype='plain', _charset='utf-8')
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ";".join(to_list)

        try:
            server = smtplib.SMTP()
            server.connect(Email.__HOST)
            server.login(Email.__USER, Email.__PWD)
            server.sendmail(me, to_list, msg.as_string())
            server.close()

            return True
        except smtplib.SMTPException:
            return False


if __name__ == '__main__':
    base = '/Users/luoyanjie/IdeaProjects/'  # local
    # base = '/root/zSky/'  # stable
    # base = '/root/zSky/'  # prod

    obj = ClearOldLog()
    obj.handle(base + 'logs/cloud-logs/',
               [
                   'admin-web',
                   'auth',
                   'auth-web',
                   'cloud-web',
                   'eye-web',
                   'operation-web'
               ])
