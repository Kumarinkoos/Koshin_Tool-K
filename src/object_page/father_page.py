"""
页面的父类
菜单页面、帮助页面、内容页面都继承这个页面父类
页面父类定义了：
    标签框架（__top_frame）
    分割线（__seq）
    标题标签（__title_label）,需要传参数title属性
    Powered标签（__powered_by_label）

    并已经将标题标签和Powered标签放入标签框架了，
    子类只需要给title的值就可以初始化。
    由于每个销毁页面的框架都不同，所以销毁页面的方法不建议重写
@ author: Kumarinko
@ version: 1.0.0
@ date: 2022-11-04
"""
from tkinter import *
import tkinter.ttk as ttk
# 测试用
import test


class FatherPage:
    # 类的属性
    title = None

    # 类的方法
    # 初始化框架
    def __init__(self, master: Tk):
        self.master = master
        # 初始化标签框架（top_frame)
        self.__top_frame = Frame(self.master, bg="white", width=800, height=49)
        self.__top_frame.place(x=0, y=0)
        # 初始化分割线
        self.__seq = ttk.Separator(self.master, orient=HORIZONTAL)
        self.__seq.pack(pady=50, fill="x")

    # 标题标签和Powered标签放在顶端框架
    def title_label_in_top_frame(self, title: str):
        self.title = title
        # 标签框架里调用标题标签和Powered By标签
        self.__create_title_label(title)
        self.__create_powered_label()

    # 标题标签
    def __create_title_label(self, title: str):
        self.__title_label = Label(self.__top_frame, text=title, font="微软雅黑", bg="white")
        self.__title_label.place(x=20, y=10)

    # Powered By标签
    def __create_powered_label(self):
        self.__powered_by_label = Label(self.__top_frame, text="Powered By Kumarinko", bg="white", fg="#A0AFB7")
        self.__powered_by_label.place(x=630, y=20)

    def destroy_page(self):
        self.__top_frame.destroy()
        self.__seq.destroy()


if __name__ == '__main__':
    root = Tk()
    test.root_test(root, "父类页测试")
    father_page = FatherPage(root)
    father_page.title = "父类测试"
    father_page.title_label_in_top_frame(father_page.title)
    root.mainloop()
