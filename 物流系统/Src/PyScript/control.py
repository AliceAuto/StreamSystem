from ui import Win as UI
class Controller:
    """应用程序控制器。"""
    def __init__(self):
        self.ui = None

    def init(self, ui):
        self.ui = ui

    def User_Info(self):
        print("Open User_Info")

    def login(self):
        # 调用 WinGUI 的 login_success 方法以切换到主页面
        if self.ui.login_frame:  # 确保登录框存在
            self.ui.on_login_success()
        print("Open login")

    def register(self):
        print("Open registration")
