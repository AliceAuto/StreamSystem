from ui import WinGUI as UI
class Controller:
    ui: UI

    def __init__(self):
        pass

    def init(self, ui):
        self.ui = ui

    def User_Info(self):
        print("Oppen User_Info")

    def login(self, evt):
        self.ui.login_success() # 调用 WinGUI 的 login_success 方法以切换到主页面
        print("OPpen login")

    def zhuce(self, evt):
        print("Open zhuce")
