"""
菜单页面，用于选择各个功能
继承于father page，不被其他页面继承
框架主要包括顶部标签用框架、按钮框架、提示框架
由于页面父类已经定义好了标签框架和分割线，所以只需要给title就可以进行初始化
菜单页面定义了：
    按钮阵列框架（__button_frame）
    提示框架（__tips_frame）
    按钮阵列并布局到了按钮阵列框架
    各按钮的提示标签并布局到了提示框架
    由于设定了提示标签在鼠标在对应按钮上时才显示，所以一开始设定了隐藏提示标签
    并绑定了鼠标进出事件，鼠标进入显示，鼠标出去隐藏
    由于menu page不被其他页面继承，所以销毁页面也不会被重写
@ author: Kumarinko
@ version: 1.0.0
@ date: 2022-11-04
"""
from tkinter import *
from src.object_page import father_page
from src.help_page import help_page
from src.find_page import find_page
from src.report_page import report_step1_page


class MenuPage(father_page.FatherPage):
    # 类的属性
    title = "菜单"
    # 按钮文字
    __find_button_txt = "找寻文件模板".center(6)
    __report_button_txt = "试验报告书".center(6)
    __help_button_txt = "帮助文档".center(6)
    # 提示框文字
    __find_text = "找寻文件模板"
    __report_text = "试验报告书"
    __help_text = "帮助文档"

    # 类的方法
    # 初始化框架及放置父类框架
    def __init__(self, master: Tk):
        super().__init__(master)
        self.master = master
        # 初始化框架
        # 初始化标签框架（top_frame）和分割线同时设置标题
        super().title_label_in_top_frame(self.title)
        # 初始化按钮框架（button_frame)
        self.__button_frame = Frame(self.master, bg="white", width=600, height=400)
        self.__button_frame.place(x=0, y=51)
        # 初始化提示框架（tips_frame)
        self.__tips_frame = LabelFrame(self.master, text="提示", labelanchor="n", font=("微软雅黑", 12),
                                       bg="white", width=190, height=380)
        self.__tips_frame.place(x=600, y=51)
        # 初始化按钮
        self.__find_button = Button(self.__button_frame, text=self.__find_button_txt, width=10, height=2,
                                    font=("微软雅黑", 18), bg="#89CFF0", command=self.__change_find_page)
        self.__report_button = Button(self.__button_frame, text=self.__report_button_txt, width=10, height=2,
                                      font=("微软雅黑", 18), bg="#89CFF0", command=self.__change_report_page)
        self.__help_button = Button(self.__button_frame, text=self.__help_button_txt, width=10, height=2,
                                    font=("微软雅黑", 18), bg="#89CFF0", command=self.__change_help_page)
        # 初始化提示文本
        self.__find_label = Label(self.__tips_frame, text=self.__find_text, bg="white")
        self.__report_label = Label(self.__tips_frame, text=self.__report_text, bg="white")
        self.__help_label = Label(self.__tips_frame, text=self.__help_text, bg="white")

    # 按钮框架
    def button_in_button_frame(self):
        # 找寻文件模板按钮
        self.__find_button.grid(row=0, column=0, padx=20, pady=15)
        self.__find_button.bind("<Enter>", func=self.__find_mouse_in)
        self.__find_button.bind("<Leave>", func=self.__find_mouse_out)
        # 试验报告书按钮
        self.__report_button.grid(row=0, column=1, padx=20, pady=15)
        self.__report_button.bind("<Enter>", func=self.__report_mouse_in)
        self.__report_button.bind("<Leave>", func=self.__report_mouse_out)
        # 帮助文档按钮
        self.__help_button.grid(row=0, column=2, padx=20, pady=15)
        self.__help_button.bind("<Enter>", func=self.__help_mouse_in)
        self.__help_button.bind("<Leave>", func=self.__help_mouse_out)

    # 提示框架
    def tips_label_in_tips_frame(self):
        # 提示框内鼠标不在按钮上为隐藏
        self.__find_label.place_forget()
        self.__report_label.place_forget()
        self.__help_label.place_forget()

    # 鼠标进出事件
    def __find_mouse_in(self, event):
        self.__find_label.place(x=0, y=0)

    def __find_mouse_out(self, event):
        self.__find_label.place_forget()

    def __report_mouse_in(self, event):
        self.__report_label.place(x=0, y=0)

    def __report_mouse_out(self, event):
        self.__report_label.place_forget()

    def __help_mouse_in(self, event):
        self.__help_label.place(x=0, y=0)

    def __help_mouse_out(self, event):
        self.__help_label.place_forget()

    # 鼠标点击换页
    def __change_find_page(self):
        self.__destroy_page()
        find_p = find_page.FindPage(self.master)
        find_p.func_in_content_frame()
        find_p.jump_button_in_under_frame()

    def __change_report_page(self):
        self.__destroy_page()
        report_step1_p = report_step1_page.ReportStep1(self.master)
        report_step1_p.func_in_content_frame()
        report_step1_p.jump_button_in_under_frame()

    def __change_help_page(self):
        self.__destroy_page()
        help_p = help_page.HelpPage(self.master)
        help_p.notebook_in_cut()
        help_p.return_button_in_under_frame()

    # 销毁页面
    def __destroy_page(self):
        super().destroy_page()
        self.__button_frame.destroy()
        self.__tips_frame.destroy()


if __name__ == '__main__':
    root = Tk()
    root.title("菜单页测试")
    # 设置窗口大小
    width = 800
    height = 450
    scree_center_width = int((root.winfo_screenwidth() - width) / 2)
    scree_center_height = int((root.winfo_screenheight() - height) / 2)
    root.geometry(f"{width}x{height}+{scree_center_width}+{scree_center_height}")

    # 设置背景为颜色
    root.config(background="white")

    # 窗口不可放大
    root.resizable(False, False)
    menu_page = MenuPage(root)
    menu_page.button_in_button_frame()
    menu_page.tips_label_in_tips_frame()
    root.mainloop()
