# coding: utf-8
"""
项目配置文件
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
各项参数配置
"""


class Config:
    APP_NAME = "pyapi_dev"
    APP_VERSION = "0123456789"
    APP_UPDATE_TIME = "2020-08-22 00:15:23"
    SECRET_KEY = "flask_cli start"

    SQLALCHEMY_POOL_SIZE = 100      # 连接池个数
    SQLALCHEMY_POOL_TIMEOUT = 30    # 超时时间，秒
    SQLALCHEMY_POOL_RECYCLE = 3600  # 空连接回收时间，秒
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    LOG_LEVEL = 10
    # 查询时会显示原始SQL语句
    # SQLALCHEMY_ECHO = True
    MYSQL_USERNAME = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = 3306
    DATA_BASE = 'mood'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(MYSQL_USERNAME,
                                                                      MYSQL_PASSWORD,
                                                                      MYSQL_HOST, MYSQL_PORT,
                                                                      DATA_BASE)


class TestingConfig(Config):
    TESTING = True
    LOG_LEVEL = 10
    MYSQL_USERNAME = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = 3306
    DATA_BASE = 'mood'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(MYSQL_USERNAME,
                                                                      MYSQL_PASSWORD,
                                                                      MYSQL_HOST, MYSQL_PORT,
                                                                      DATA_BASE)


class ProductionConfig(Config):
    MYSQL_USERNAME = 'root'
    MYSQL_PASSWORD = '123456'
    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = 3306
    DATA_BASE = 'mood'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(MYSQL_USERNAME,
                                                                      MYSQL_PASSWORD,
                                                                      MYSQL_HOST, MYSQL_PORT,
                                                                      DATA_BASE)


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
