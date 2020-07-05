from appservice import AppServer
import routinemgr

if __name__ == '__main__':
    # 创建应用服务
    appServer = AppServer.Instance()
    # 启动
    appServer.Run()
