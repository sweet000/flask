import logging
from flask import Flask,redirect,url_for,render_template,request,session
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from info import create_app, db  

app = create_app("development")
# manager启动服务命令
manager = Manager(app)
#数据库db和app关联起来
Migrate(app,db)
#将迁移命令集成的manager中
manager.add_command('db',MigrateCommand)
    
@app.route('/',methods=['GET','POST'])
def home():
    logging.debug("测试debug")
    logging.warning("测试warning")
    logging.error("测试error")
    logging.fatal("测试fatal")
    
    session["dj"] = "test"
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return 'hello'

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    manager.run()