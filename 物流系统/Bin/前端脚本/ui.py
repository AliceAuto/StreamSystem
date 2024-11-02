from tkinter import *
from tkinter.ttk import *
import random
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        
        # 定义登录界面
        self.login_frame = Frame(self)
        self.tk_label_frame_Label_C = self.__tk_label_frame_Label_C(self.login_frame)
        self.tk_label_Account_Label = self.__tk_label_Account_Label(self.tk_label_frame_Label_C) 
        self.tk_label_PassWard_Label = self.__tk_label_PassWard_Label(self.tk_label_frame_Label_C) 
        self.tk_input_Account_Input = self.__tk_input_Account_Input(self.tk_label_frame_Label_C) 
        self.tk_input_PassWard_Input = self.__tk_input_PassWard_Input(self.tk_label_frame_Label_C) 
        self.tk_button_Login_Button = self.__tk_button_Login_Button(self.tk_label_frame_Label_C) 
        self.tk_button_Register_Button = self.__tk_button_Register_Button(self.tk_label_frame_Label_C) 
        self.tk_label_SignLabel_Label = self.__tk_label_SignLabel_Label(self.login_frame)
        
        self.login_frame.place(x=0, y=0, relwidth=1, relheight=1)
        
        # 定义主页面
        self.main_page = Frame(self)
        self.tk_label_frame_Lable_C1 = self.__tk_label_frame_Lable_C1(self.main_page)
        self.tk_label_frame_Head_C2 = self.__tk_label_frame_Head_C2(self.tk_label_frame_Lable_C1)
        self.tk_table_Head_Table = self.__tk_table_Head_Table(self.tk_label_frame_Head_C2)
        self.tk_label_frame_Data_C = self.__tk_label_frame_Data_C(self.tk_label_frame_Lable_C1)
        self.tk_text_Data_Text = self.__tk_text_Data_Text(self.tk_label_frame_Data_C)
        self.tk_label_frame_Status_C = self.__tk_label_frame_Status_C(self.main_page)
        self.tk_progressbar_lucekizw = self.__tk_progressbar_lucekizw(self.main_page)

        # 创建一个用于显示网格的Frame
        self.grid_frame = Frame(self.main_page)
        self.grid_frame.place(x=12, y=320, width=636, height=200)  # 位置和大小可以根据需要调整
        self.draw_grid(self.grid_frame, rows=5, cols=5)  # 在grid_frame中绘制网格

        # 创建节点地图
        self.node_map_frame = Frame(self.main_page)
        self.node_map_frame.place(x=12, y=50, width=636, height=250)  # 设置节点地图的位置和大小
        self.node_map = NodeMap(self.node_map_frame)  # 创建节点地图
        self.node_map.pack(fill=BOTH, expand=True)  # 确保节点地图填充整个frame

        self.main_page.place_forget()  # 初始隐藏主页面

    def draw_grid(self, parent, rows, cols):
        """绘制二维网格，用随机颜色填充单元格."""
        for r in range(rows):
            for c in range(cols):
                # 生成随机颜色
                color = "#{:06x}".format(random.randint(0, 0xFFFFFF))  # 生成随机颜色代码
                # 创建一个画布用于绘制方块
                cell = Canvas(parent, width=60, height=60, bg=color, borderwidth=1, relief="solid")
                cell.grid(row=r, column=c, padx=5, pady=5)  # 使用 grid 布局管理器

    def __win(self):
        self.title("物流系统客户端")
        width, height = 1100, 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    # 切换到主页面的方法
    def show_main_page(self):
        self.login_frame.place_forget()  # 隐藏登录页面
        self.main_page.place(x=0, y=0, relwidth=1, relheight=1)  # 显示主页面

    # 登录成功后的事件方法
    def login_success(self, event=None):
        self.show_main_page()

    def __tk_label_frame_Label_C(self, parent):
        frame = LabelFrame(parent, text="管理员")
        frame.place(x=31, y=60, width=317, height=185)
        return frame

    def __tk_label_Account_Label(self, parent):
        label = Label(parent, text="账号：", anchor="center")
        label.place(x=22, y=12, width=50, height=30)
        return label

    def __tk_label_PassWard_Label(self, parent):
        label = Label(parent, text="密码：", anchor="center")
        label.place(x=22, y=62, width=50, height=30)
        return label

    def __tk_input_Account_Input(self, parent):
        ipt = Entry(parent)
        ipt.place(x=88, y=11, width=196, height=30)
        return ipt

    def __tk_input_PassWard_Input(self, parent):
        ipt = Entry(parent)
        ipt.place(x=88, y=63, width=196, height=30)
        return ipt

    def __tk_button_Login_Button(self, parent):
        btn = Button(parent, text="登录", takefocus=False)
        btn.place(x=80, y=114, width=71, height=30)
        btn.bind('<Button-1>', self.login_success)  # 绑定登录按钮事件，模拟登录成功
        return btn

    def __tk_button_Register_Button(self, parent):
        btn = Button(parent, text="注册", takefocus=False)
        btn.place(x=194, y=114, width=67, height=30)
        return btn

    def __tk_label_SignLabel_Label(self, parent):
        label = Label(parent, text="物流系统客户端", anchor="center")
        label.place(x=381, y=7, width=309, height=30)
        return label

    def __tk_label_frame_Lable_C1(self, parent):
        frame = LabelFrame(parent, text="Information")
        frame.place(x=402, y=89, width=665, height=387)
        return frame

    def __tk_label_frame_Head_C2(self, parent):
        frame = LabelFrame(parent, text="Head")
        frame.place(x=15, y=24, width=633, height=91)
        return frame

    def __tk_table_Head_Table(self, parent):
        columns = {"Account": 213, "Power": 183, "Name": 213}
        tk_table = Treeview(parent, show="headings", columns=list(columns))
        for text, width in columns.items():
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)
        tk_table.place(x=10, y=13, width=612, height=46)
        return tk_table

    def __tk_label_frame_Data_C(self, parent):
        frame = LabelFrame(parent, text="Data")
        frame.place(x=12, y=132, width=636, height=228)
        return frame

    def __tk_text_Data_Text(self, parent):
        text = Text(parent)
        text.place(x=17, y=15, width=602, height=176)
        return text

    def __tk_label_frame_Status_C(self, parent):
        frame = LabelFrame(parent, text="Status")
        frame.place(x=15, y=280, width=355, height=192)
        return frame

    def __tk_progressbar_lucekizw(self, parent):
        progressbar = Progressbar(parent, orient=HORIZONTAL)
        progressbar.place(x=436, y=46, width=599, height=30)
        return progressbar


class NodeMap(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.canvas = Canvas(self, bg="white")
        self.canvas.pack(fill=BOTH, expand=True)  # 填充整个NodeMap区域
        
        # 创建节点和连接
        self.nodes = {}
        self.edges = []
        self.create_nodes(5)  # 创建5个节点
        self.draw_edges()
        
    def create_nodes(self, num_nodes):
        """创建指定数量的节点并随机放置在画布上。"""
        for i in range(num_nodes):
            x = random.randint(50, 750)
            y = random.randint(50, 550)
            node_id = self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="blue")
            self.nodes[node_id] = (x, y)
            self.canvas.tag_bind(node_id, "<Button-1>", self.show_node_info)  # 绑定单击事件
    
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
        line_id = self.canvas.create_line(x1, y1, x2, y2, fill="black", width=2)
        self.edges.append(line_id)
    
    def show_node_info(self, event):
        """在单击节点时显示节点信息。"""
        node_id = self.canvas.find_withtag(CURRENT)[0]
        x, y = self.nodes[node_id]
        print(f"Node {node_id} at ({x}, {y})")  # 你可以改为弹出窗口或其他方式显示信息

class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.config(menu=self.create_menu())
        self.ctl.init(self)
    def create_menu(self):
        menu = Menu(self,tearoff=False)
        menu.add_cascade(label="Inter",menu=self.menu_luce81z6(menu))
        return menu
    def menu_luce81z6(self,parent):
        menu = Menu(parent,tearoff=False)
        menu.add_command(label="User-Info",command=self.ctl.User_Info)
        return menu
    def __event_bind(self):
        self.tk_button_Login_Button.bind('<Button-1>',self.ctl.login)
        self.tk_button_Register_Button.bind('<Button-1>',self.ctl.zhuce)
        pass
    def __style_config(self):
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()