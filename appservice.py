from flask import Flask
from flask.ext.login import LoginManager
import threading

# 应用服务
class AppServer(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        print(__name__)
        self.__app = Flask(__name__)
        self.__app.config.from_pyfile("configs/webconfig.ini")
        #self.__loginMgr = LoginManager()
        #self.__loginMgr.login_view = "sign_in"
        #self.__loginMgr.init_app(self.__app)

    # 单例
    @classmethod
    def Instance(cls, *args, **kwargs):
        with AppServer._instance_lock:
            if not hasattr(AppServer, "_instance"):
                AppServer._instance = AppServer(*args, **kwargs)
        return AppServer._instance
    
    def GetFlask(self):
        return self.__app
    
    def Run(self):
        self.__app.run()
