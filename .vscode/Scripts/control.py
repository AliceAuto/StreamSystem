class Controller:
    ui: WinGUI

    def __init__(self):
        pass

    def init(self, ui):
        self.ui = ui

    def User_Info(self):
        print("点击了菜单")

    def login(self, evt):
        username = self.ui.tk_input_Account_Input.get()
        password = self.ui.tk_input_PassWard_Input.get()

        if not username or not password:
            self.ui.show_error("账号和密码不能为空！")
            return

        # 模拟后端验证
        if self.validate_user(username, password):
            self.ui.show_message("登录成功！")
            # 这里可以继续进行其他操作，如跳转到主界面
        else:
            self.ui.show_error("账号或密码错误！")

    def zhuce(self, evt):
        print("<Button-1>事件未处理:", evt)

    def validate_user(self, username, password):
        # 模拟一个简单的验证逻辑，这里应该与后端进行实际的验证
        return username == "admin" and password == "password"  # 示例：只接受 admin/password
