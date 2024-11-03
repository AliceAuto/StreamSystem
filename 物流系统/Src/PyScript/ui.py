from tkinter import *
from tkinter.ttk import *
import random

class BaseFrame(Frame):
    """基础框架类，所有框架的基类。"""
    def __init__(self, parent):
        super().__init__(parent)

class LoginFrame(BaseFrame):
    """登录界面类。"""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller  # 保存控制器实例
        self.__create_widgets()

    def __create_widgets(self):
        """创建登录界面的组件。"""
        admin_label_frame = LabelFrame(self, text="管理员")
        admin_label_frame.place(x=31, y=60, width=317, height=185)

        Label(admin_label_frame, text="账号：").place(x=22, y=12, width=50, height=30)
        self.account_input = Entry(admin_label_frame)
        self.account_input.place(x=88, y=11, width=196, height=30)

        Label(admin_label_frame, text="密码：").place(x=22, y=62, width=50, height=30)
        self.password_input = Entry(admin_label_frame, show="*")
        self.password_input.place(x=88, y=63, width=196, height=30)

        Button(admin_label_frame, text="登录", command=self.controller.login).place(x=80, y=114, width=71, height=30)
        Button(admin_label_frame, text="注册", command=self.controller.register).place(x=194, y=114, width=67, height=30)

        Label(self, text="物流系统客户端").place(x=381, y=7, width=309, height=30)

class MainPage(BaseFrame):
    """主页面类。"""
    def __init__(self, parent):
        super().__init__(parent)
        self.__create_widgets()

    def __create_widgets(self):
        """创建主页面的组件。"""
        # 信息框
        info_label_frame = LabelFrame(self, text="Information")
        info_label_frame.place(x=402, y=89, width=665, height=387)

        # 创建表头框
        head_label_frame = LabelFrame(self, text="Head")
        head_label_frame.place(x=15, y=24, width=633, height=91)
        self.head_table = self.__create_head_table(head_label_frame)

        # 创建数据框
        data_label_frame = LabelFrame(self, text="Data")
        data_label_frame.place(x=12, y=132, width=636, height=228)
        self.data_text = Text(data_label_frame, width=70, height=10)
        self.data_text.pack()

        # 创建状态框
        status_label_frame = LabelFrame(self, text="Status")
        status_label_frame.place(x=15, y=280, width=355, height=192)
        self.progressbar = Progressbar(status_label_frame, orient=HORIZONTAL)
        self.progressbar.place(x=10, y=20, width=300, height=30)

        # 创建网格和节点地图
        self.grid_frame = Frame(self)
        self.grid_frame.place(x=12, y=320, width=636, height=200)
        self.draw_grid(self.grid_frame, rows=5, cols=5)

        self.node_map = NodeMap(self)
        self.node_map.place(x=12, y=50, width=636, height=250)

    def draw_grid(self, parent, rows, cols):
        """绘制二维网格，用随机颜色填充单元格。"""
        for r in range(rows):
            for c in range(cols):
                color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
                cell = Canvas(parent, width=60, height=60, bg=color, borderwidth=1, relief="solid")
                cell.grid(row=r, column=c, padx=5, pady=5)

    def __create_head_table(self, parent):
        """创建表头及其列。"""
        columns = {"Account": 213, "Power": 183, "Name": 213}
        tk_table = Treeview(parent, show="headings", columns=list(columns))
        for text, width in columns.items():
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)
        tk_table.place(x=10, y=13, width=612, height=46)
        return tk_table

class NodeMap(BaseFrame):
    """节点地图类，负责绘制节点和边。"""
    def __init__(self, parent):
        super().__init__(parent)
        self.__create_canvas()
        self.create_nodes(5)  # 创建5个节点
        self.draw_edges()

    def __create_canvas(self):
        """创建画布。"""
        self.canvas = Canvas(self, bg="white")
        self.canvas.place(x=0, y=0, width=700, height=250)
        self.canvas.create_rectangle(0, 0, 638, 250, outline="black", width=10)

        self.nodes = {}
        self.edges = []

    def create_nodes(self, num_nodes):
        """创建指定数量的节点并随机放置在画布上。"""
        for i in range(num_nodes):
            x = random.randint(50, 100)
            y = random.randint(50, 100)
            node_id = self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="blue")
            self.canvas.create_text(x, y, text=str(i + 1), font=("Arial", 12), fill="white")
            self.nodes[node_id] = (x, y)
            self.canvas.tag_bind(node_id, "<Button-1>", self.show_node_info)

    def draw_edges(self):
        """绘制随机连接的边。"""
        node_ids = list(self.nodes.keys())
        for i in range(len(node_ids)):
            for j in range(i + 1, len(node_ids)):
                if random.choice([True, False]):  # 随机连接一些节点
                    self.connect_nodes(node_ids[i], node_ids[j])

    def connect_nodes(self, node1_id, node2_id):
        """连接两个节点并绘制边。"""
        x1, y1 = self.nodes[node1_id]
        x2, y2 = self.nodes[node2_id]
        self.canvas.create_line(x1, y1, x2, y2, fill="black", width=2)
    
    def show_node_info(self, event):
        """在单击节点时显示节点信息。"""
        node_id = self.canvas.find_withtag(CURRENT)[0]
        x, y = self.nodes[node_id]
        print(f"Node {node_id} at ({x}, {y})")

class Win(Tk):
    """主窗口类，负责运行应用程序。"""
    def __init__(self, controller):
        super().__init__()
        self.title("物流系统客户端")
        self.geometry("1650x900")
        self.resizable(width=False, height=False)

        self.controller = controller  # 保存控制器实例
        self.login_frame = LoginFrame(self, self.controller)
        self.login_frame.pack(fill=BOTH, expand=True)

        self.main_page = MainPage(self)

    def on_login_success(self):
        """处理登录成功事件，切换到主页面。"""
        self.login_frame.pack_forget()  # 隐藏登录页面
        self.main_page.pack(fill=BOTH, expand=True)