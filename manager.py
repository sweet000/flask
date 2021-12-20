from logging import DEBUG
from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy

class Config(object):
    # 项目的配置
    DEBUG = True
    
    #为数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/information27"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
app=Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run()