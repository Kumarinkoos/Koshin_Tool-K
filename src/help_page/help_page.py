"""
关于这个软件的界面，用于现实帮助文档（使用Notebook控件）
继承于father page，不被其他页面继承
框架主要包括顶部标签用框架、Notebook框架、底层返回按钮框架
由于页面父类已经定义好了标签框架和分割线，所以只需要给title就可以进行初始化
帮助文档页面定义了：
    选项卡框架（__cut_frame）
    底部框架（__under_frame）
    各个选项卡并布局到了选项卡框架中
    返回按钮（__return_button）并布局到了底部框架
    由于help page不被其他页面继承，所以销毁页面也不会被重写
@ author: Kumarinko
@ version: 1.0.0
@ date: 2022-11-04
"""
from tkinter import *
import tkinter.ttk as ttk
from src.object_page import father_page
from src.menu_page import menu_page


class HelpPage(father_page.FatherPage):
    # 类的属性
    title = "帮助文档"
    # 跳转按钮文字
    __return_button_txt = "返回主菜单"
    # 选项卡标题
    __title_find = "关于找寻文件模板".center(20)
    __title_report = "关于试验报告书".center(20)
    __title_about = "关于这个软件".center(20)
    # 选项卡内容
    __find_info_text = "找寻文件"
    __report_info_text = "试验报告书"
    __about_info_text = "关于这个软件"

    # 类的方法
    # 初始化框架及放置父类框架
    def __init__(self, master: Tk):
        super().__init__(master)
        self.master = master
        # 初始化框架
        # 初始化标签框架（top_frame）和分割线同时设置标题
        super().title_label_in_top_frame(self.title)
        # 初始化选项卡（cut_frame
        self.__cut_frame = ttk.Notebook(self.master, width=800, height=300)
        self.__cut_frame.place(x=0, y=51)
        # 初始化跳转框架（under_frame)
        self.__under_frame = Frame(self.master, bg="white", width=800, height=100)
        self.__under_frame.place(x=0, y=350)
        # 初始化按钮
        self.__return_button = Button(self.__under_frame, text=self.__return_button_txt, width=10, height=2,
                                      font=("微软雅黑", 12), bg="#89CFF0", command=self.__help_return_menu)

    # 选项卡框架
    def notebook_in_cut(self):
        # 选项卡放置
        self.__create_find_notebook()
        self.__create_report_notebook()
        self.__create_about_notebook()

    # 返回按钮框架
    def return_button_in_under_frame(self):
        # 返回按钮放置
        self.__return_button.place(x=40, y=15)

    # 关于找寻文件模板
    def __create_find_notebook(self):
        # 关于找寻文本模板的选项卡的添加
        self.__cut_find_frame = Frame(self.__cut_frame)
        self.__cut_frame.add(self.__cut_find_frame, text=self.__title_find)

        # 关于找寻文件模板里的文本框
        self.__find_info = Text(self.__cut_find_frame, width=110, height=19)
        self.__find_info.place(x=10, y=10)
        # 插入文本
        self.__find_info.insert(0.0, self.__find_info_text)
        self.__find_info.config(state=DISABLED)

    # 关于试验报告书
    def __create_report_notebook(self):
        # 关于试验报告书选项卡的添加
        self.__cut_report_frame = Frame(self.__cut_frame)
        self.__cut_frame.add(self.__cut_report_frame, text=self.__title_report)

        # 关于试验报告书里的文本框
        self.__report_info = Text(self.__cut_report_frame, width=110, height=19)
        self.__report_info.place(x=10, y=10)
        # 插入文本
        self.__report_info.insert(0.0, self.__report_info_text)
        self.__report_info.config(state=DISABLED)

    # 关于这个软件
    def __create_about_notebook(self):
        # 关于这个软件的选项卡的添加
        self.__cut_about_frame = Frame(self.__cut_frame)
        self.__cut_frame.add(self.__cut_about_frame, text=self.__title_about)

        # 关于这个软件里的文本框
        self.__about_info = Text(self.__cut_about_frame, width=110, height=19)
        self.__about_info.place(x=10, y=10)
        # 插入文本
        self.__about_info.insert(0.0, self.__about_info_text)
        self.__about_info.config(state=DISABLED)

    # 返回主菜单按钮
    def __help_return_menu(self):
        self.__destroy_page()
        menu_p = menu_page.MenuPage(self.master)
        menu_p.button_in_button_frame()
        menu_p.tips_label_in_tips_frame()

    # 销毁页面
    def __destroy_page(self):
        super().destroy_page()
        self.__cut_frame.destroy()
        self.__under_frame.destroy()


if __name__ == '__main__':
    root = Tk()
    root.title("帮助文档测试")
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
    help_page = HelpPage(root)
    help_page.notebook_in_cut()
    help_page.return_button_in_under_frame()
    root.mainloop()
