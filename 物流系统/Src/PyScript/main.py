
from ui import Win
from control import Controller

if __name__ == "__main__":
    controller = Controller()  # 创建控制器实例
    app = Win(controller)  # 将控制器传递给主窗口                   controller ->UI
    controller.init(app)  # 初始化控制器绑定UI                      UI -> controller
    app.mainloop()  # 启动应用程序
    





