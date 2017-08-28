import pymysql


class MySQLConfig:
    """
    MySQL配置文件
    """

    PORT = 3306
    CHARSET = 'utf8mb4'
    CURSOR_CLASS = pymysql.cursors.DictCursor

    @staticmethod
    def __common_config():
        config = {
            'port': 3307,
            'charset': MySQLConfig.CHARSET,
            'cursorclass': MySQLConfig.CURSOR_CLASS
        }
        return config

    @staticmethod
    def localhost():
        config = MySQLConfig.__common_config()
        config['host'] = '127.0.0.1'
        config['user'] = 'root'
        config['password'] = '123456'
        config['db'] = 'wcs'
        return config

    @staticmethod
    def inner():
        config = MySQLConfig.__common_config()
        config['host'] = '192.168.1.101'
        config['user'] = 'itianluo'
        config['password'] = '^itianluo@0928$'
        config['db'] = 'itianluo'
        return config

    @staticmethod
    def stable():
        config = MySQLConfig.__common_config()
        config['host'] = 'localhost'
        config['user'] = 'itianluo'
        config['password'] = 'Aijia1501$'
        config['db'] = 'itianluo'
        return config
