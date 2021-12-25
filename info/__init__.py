import logging
from config import config
from logging import DEBUG, Formatter, Logger, RootLogger, log
from logging.handlers import RotatingFileHandler
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask import Flask,redirect,url_for,render_template,request,session
db = SQLAlchemy()

def setup_log(config_name):
    #设置日志的记录等级
    logging.basicConfig(level=config[config_name].LOG_LEVEL)
    # 创建日志记录器，指明日志保存的路径，每个日志文件大小，及其日志文件保存个数
    file_log_handler = RotatingFileHandler("logs/log", maxBytes = 1024 * 1024 * 10, backupCount = 10)
    #创建日志记录格式，日志等级，输入日志信息的文件名 行数，日志信息
    Formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s' )
    #为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(Formatter)
    #为全局的日志工具对象（flask app）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)

def create_app(config_name):
    setup_log(config_name)
    app=Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    redis_store = StrictRedis(host = config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)
    Session(app)
    #开启crsf项目保护
    CSRFProtect(app)
    return app