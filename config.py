from logging import debug
import logging
from re import T
from flask import config
import redis
import base64
import os

class Config(object):
    # 项目的配置
    DEBUG = True
    SECRET_KEY = base64.b64encode(os.urandom(48))
    print(SECRET_KEY)
    print(type(SECRET_KEY))
    #为数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/information27"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 添加redis配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    #session保存配置
    SESSION_TYPE = "redis"
    #开启session签名
    SESSION_USE_SIGNER = True
    #指定Session保存的redis
    SESSION_REDIS = redis.Redis(host = REDIS_HOST, port= REDIS_PORT)
    #设置需要过期时间
    SESSION_PERMANENT = False
    #设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2
    # 设置日志等级
    LOG_LEVEL = logging.ERROR
    

class Development(Config):
    debug = True
    
class Production(Config):
    debug = False
    LOG_LEVEL = logging.WARNING
    
class Testing(Config):
    debug = True
    Testing = True
    
config = {"development":Development,
          "production":Production,
          "testing":Testing}
    