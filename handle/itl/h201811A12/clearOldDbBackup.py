import os
import logging
import smtplib

from datetime import datetime
from email.mime.text import MIMEText

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='clearOldDbBackup.log',
                    filemode='a')


class clearOldDbBackup:
    __DAY = 10  # 日期阈值
    __MAIL_TO = ["546223592@qq.com", 'luoyanjie@itianluo.cn', 'huangzhen@itianluo.cn', '853467358@qq.com']  # 目标邮箱列表

    def __init__(self):
        self.log = list()
        logging.info('============> init ' + str(datetime.now()))
        self.log.append('============> init ' + str(datetime.now()))

    def handle(self, path):
        if path == '' or path is None:
            logging.info('No path data!')
            self.log.append('No path data!')
            return

        delete_file = set()

        for dir_path, dir_names, file_names in os.walk(path):
            for file_name in file_names:
                if clearOldDbBackup.need_delete(file_name):
                    delete_file.add(os.path.join(dir_path, file_name))

        self.to_delete(delete_file)

        logging.info('End. \n')
        self.log.append('End. \n')

        Email.send_mail('定时清理数据库备份', "\n".join(self.log), clearOldDbBackup.__MAIL_TO)

    @staticmethod
    def need_delete(file_name):
        result = False
        file_name_split = file_name.split('.')

        if len(file_name_split) == 3 and file_name_split[0] is not None and file_name_split[0] != '':
            log_time = datetime.strptime(file_name_split[0] + ':59.999999', '%Y%m%d%H%M:%S.%f')
            if (datetime.now() - log_time).days > clearOldDbBackup.__DAY:
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
    __ME = me = 'Thor' + '<%s>'

    @staticmethod
    def send_mail(sub, content, to_list, product='netease'):
        if product == 'netease':
            Email.netease(sub, content, to_list)
        elif product == 'tencent':
            Email.tencent(sub, content, to_list)

    @staticmethod
    def netease(sub, content, to_list):
        """
        网易邮箱发送邮件
        :param sub: 主题
        :param content: 内容
        :param to_list: 发送目标
        :return: 发送成功返回True
        """
        host = 'smtp.163.com'  # SMTP 服务器主机
        user = 'luoyanjiewade@163.com'
        pwd = ''  # 163邮箱smtp生成的密码

        me = "Thor" + "<" + user + ">"

        msg = MIMEText(content, _subtype='plain', _charset='utf-8')
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ';'.join(to_list)

        try:
            server = smtplib.SMTP()
            server.connect(host)
            server.login(user, pwd)
            server.sendmail(me, to_list, msg.as_string())
            server.close()

            return True
        except smtplib.SMTPException:
            return False

    @staticmethod
    def tencent(sub, content, to_list):
        host = 'smtp.exmail.qq.com'  # SMTP 服务器主机
        user = 'luoyanjie@itianluo.cn'
        pwd = ''

        me = "Thor" + "<" + user + ">"

        msg = MIMEText(content, _subtype='plain', _charset='utf-8')
        msg["Subject"] = sub
        msg["From"] = me
        msg["To"] = ";".join(to_list)

        try:
            server = smtplib.SMTP_SSL(host, port=465)
            server.login(user, pwd)
            server.sendmail(me, to_list, msg.as_string())
            server.close()

            return True
        except smtplib.SMTPException:
            return False


if __name__ == '__main__':
    path = '/opt/backup/'  # prod

    obj = clearOldDbBackup()
    obj.handle(path)
