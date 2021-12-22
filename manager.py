from logging import DEBUG
from flask import Flask,redirect,url_for,render_template,request,session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
import redis
from flask_session import Session
import os
import base64
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

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
    
    
        
app=Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
redis_store = StrictRedis(host = Config.REDIS_HOST, port=Config.REDIS_PORT)
Session(app)
# manager启动服务命令
manager = Manager(app)
#数据库db和app关联起来
Migrate(app,db)
#将迁移命令集成的manager中
manager.add_command('db',MigrateCommand)
#开启crsf项目保护
CSRFProtect(app)


@app.route('/',methods=['GET','POST'])
def home():
    session["dj"] = "test"
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return 'hello'

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    manager.run()