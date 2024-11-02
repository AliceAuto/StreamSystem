"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import random
from tkinter import *
from tkinter.ttk import *
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_canvas_TopLine_Label = self.__tk_canvas_TopLine_Label(self)
        self.tk_label_frame_Label_C = self.__tk_label_frame_Label_C(self)
        self.tk_label_Account_Label = self.__tk_label_Account_Label( self.tk_label_frame_Label_C) 
        self.tk_label_PassWard_Label = self.__tk_label_PassWard_Label( self.tk_label_frame_Label_C) 
        self.tk_input_Account_Input = self.__tk_input_Account_Input( self.tk_label_frame_Label_C) 
        self.tk_input_PassWard_Input = self.__tk_input_PassWard_Input( self.tk_label_frame_Label_C) 
        self.tk_button_Login_Button = self.__tk_button_Login_Button( self.tk_label_frame_Label_C) 
        self.tk_button_Register_Button = self.__tk_button_Register_Button( self.tk_label_frame_Label_C) 
        self.tk_label_SignLabel_Label = self.__tk_label_SignLabel_Label(self)
        self.tk_label_frame_Lable_C1 = self.__tk_label_frame_Lable_C1(self)
        self.tk_label_frame_Head_C2 = self.__tk_label_frame_Head_C2( self.tk_label_frame_Lable_C1) 
        self.tk_table_Head_Table = self.__tk_table_Head_Table( self.tk_label_frame_Head_C2) 
        self.tk_label_frame_Data_C = self.__tk_label_frame_Data_C( self.tk_label_frame_Lable_C1) 
        self.tk_text_Data_Text = self.__tk_text_Data_Text( self.tk_label_frame_Data_C) 
        self.tk_label_frame_Status_C = self.__tk_label_frame_Status_C(self)
        self.tk_label_lucef0wa = self.__tk_label_lucef0wa( self.tk_label_frame_Status_C) 
        self.tk_check_button_lucefks9 = self.__tk_check_button_lucefks9( self.tk_label_frame_Status_C) 
        self.tk_check_button_lucefvwj = self.__tk_check_button_lucefvwj( self.tk_label_frame_Status_C) 
        self.tk_check_button_lucefx0b = self.__tk_check_button_lucefx0b( self.tk_label_frame_Status_C) 
        self.tk_check_button_lucefxs5 = self.__tk_check_button_lucefxs5( self.tk_label_frame_Status_C) 
        self.tk_label_luceiieq = self.__tk_label_luceiieq( self.tk_label_frame_Status_C) 
        self.tk_label_luceijap = self.__tk_label_luceijap( self.tk_label_frame_Status_C) 
        self.tk_label_luceik3v = self.__tk_label_luceik3v( self.tk_label_frame_Status_C) 
        self.tk_progressbar_lucekizw = self.__tk_progressbar_lucekizw(self)
    def __win(self):
        self.title("Tkinter布局助手")
        # 设置窗口大小、居中
        width = 1100
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.resizable(width=False, height=False)
        
    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def __tk_canvas_TopLine_Label(self,parent):
        canvas = Canvas(parent,bg="#aaa")
        canvas.place(x=0, y=0, width=1099, height=44)
        return canvas
    def __tk_label_frame_Label_C(self,parent):
        frame = LabelFrame(parent,text="管理员",)
        frame.place(x=31, y=60, width=317, height=185)
        return frame
    def __tk_label_Account_Label(self,parent):
        label = Label(parent,text="账号：",anchor="center", )
        label.place(x=22, y=12, width=50, height=30)
        return label
    def __tk_label_PassWard_Label(self,parent):
        label = Label(parent,text="密码：",anchor="center", )
        label.place(x=22, y=62, width=50, height=30)
        return label
    def __tk_input_Account_Input(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=88, y=11, width=196, height=30)
        return ipt
    def __tk_input_PassWard_Input(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=88, y=63, width=196, height=30)
        return ipt
    def __tk_button_Login_Button(self,parent):
        btn = Button(parent, text="登录", takefocus=False,)
        btn.place(x=80, y=114, width=71, height=30)
        return btn
    def __tk_button_Register_Button(self,parent):
        btn = Button(parent, text="注册", takefocus=False,)
        btn.place(x=194, y=114, width=67, height=30)
        return btn
    def __tk_label_SignLabel_Label(self,parent):
        label = Label(parent,text="物流系统客户端",anchor="center", )
        label.place(x=381, y=7, width=309, height=30)
        return label
    def __tk_label_frame_Lable_C1(self,parent):
        frame = LabelFrame(parent,text="Information",)
        frame.place(x=402, y=89, width=665, height=387)
        return frame
    def __tk_label_frame_Head_C2(self,parent):
        frame = LabelFrame(parent,text="Head",)
        frame.place(x=15, y=24, width=633, height=91)
        return frame
    def __tk_table_Head_Table(self,parent):
        # 表头字段 表头宽度
        columns = {"Account":213,"Power":183,"Name":213}
        tk_table = Treeview(parent, show="headings", columns=list(columns),)
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸
        
        tk_table.place(x=10, y=13, width=612, height=46)
        self.create_bar(parent, tk_table,True, True,10, 13, 612,46,633,91)
        return tk_table
    def __tk_label_frame_Data_C(self,parent):
        frame = LabelFrame(parent,text="Data",)
        frame.place(x=12, y=132, width=636, height=228)
        return frame
    def __tk_text_Data_Text(self,parent):
        text = Text(parent)
        text.place(x=17, y=15, width=602, height=176)
        self.create_bar(parent, text,True, False, 17, 15, 602,176,636,228)
        return text
    def __tk_label_frame_Status_C(self,parent):
        frame = LabelFrame(parent,text="Status",)
        frame.place(x=15, y=280, width=355, height=192)
        return frame
    def __tk_label_lucef0wa(self,parent):
        label = Label(parent,text="开关1：",anchor="center", )
        label.place(x=57, y=11, width=39, height=30)
        return label
    def __tk_check_button_lucefks9(self,parent):
        cb = Checkbutton(parent,text="多选框",)
        cb.place(x=146, y=11, width=68, height=30)
        return cb
    def __tk_check_button_lucefvwj(self,parent):
        cb = Checkbutton(parent,text="多选框",)
        cb.place(x=146, y=91, width=68, height=30)
        return cb
    def __tk_check_button_lucefx0b(self,parent):
        cb = Checkbutton(parent,text="多选框",)
        cb.place(x=146, y=131, width=68, height=30)
        return cb
    def __tk_check_button_lucefxs5(self,parent):
        cb = Checkbutton(parent,text="多选框",)
        cb.place(x=146, y=51, width=68, height=30)
        return cb
    def __tk_label_luceiieq(self,parent):
        label = Label(parent,text="开关2：",anchor="center", )
        label.place(x=57, y=52, width=39, height=30)
        return label
    def __tk_label_luceijap(self,parent):
        label = Label(parent,text="开关3：",anchor="center", )
        label.place(x=57, y=91, width=39, height=30)
        return label
    def __tk_label_luceik3v(self,parent):
        label = Label(parent,text="开关4：",anchor="center", )
        label.place(x=57, y=131, width=39, height=30)
        return label
    def __tk_progressbar_lucekizw(self,parent):
        progressbar = Progressbar(parent, orient=HORIZONTAL,)
        progressbar.place(x=436, y=46, width=599, height=30)
        return progressbar
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