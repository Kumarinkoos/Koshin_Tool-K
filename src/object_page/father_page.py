"""
页面的父类
菜单页面、帮助页面、内容页面都继承这个页面父类
@ author: Kumarinko
@ version: 1.0.0
@ date: 2022-11-04
"""
from tkinter import *
import tkinter.ttk as ttk


class FatherPage:
    # 类的属性
    title = None

    # 类的方法
    # 初始化框架
    def __init__(self, master: Tk):
        self.master = master
        self.__top_frame = Frame(self.master, bg="white", width=800, height=49)
        self.__seq = ttk.Separator(self.master, orient=HORIZONTAL)

    # 标签框架
    def create_label_frame(self, title: str):
        # 放置标签框架
        self.__top_frame.place(x=0, y=0)
        # 标签框架里调用标题标签和Powered By标签
        self.title = title
        self.__create_title_label(title)
        self.__create_powered_label()

    # 分割线
    def create_seq(self):
        # 分割线放置
        self.__seq.pack(pady=50, fill="x")

    # 标题标签
    def __create_title_label(self, title: str):
        self.__title_label = Label(self.__top_frame, text=title, font="微软雅黑", bg="white")
        self.__title_label.place(x=20, y=10)

    # Powered By标签
    def __create_powered_label(self):
        self.__powered_by = Label(self.__top_frame, text="Powered By Kumarinko", bg="white", fg="#A0AFB7")
        self.__powered_by.place(x=630, y=20)


if __name__ == '__main__':
    root = Tk()
    root.title("父类页测试")
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
    father_page = FatherPage(root)
    father_page.title = "父类测试"
    father_page.create_label_frame(father_page.title)
    father_page.create_seq()
    root.mainloop()
