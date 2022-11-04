"""
内容页父类，用于给具体的页面继承
继承于father page，给各具体内容页继承
框架主要包括顶部标签用框架、内容框架、提示框架、返回框架
@ author: Kumarinko
@ version: 1.0.0
@ date: 2022-11-04
"""
from tkinter import *
from src.object_page import father_page


class ContentPage(father_page.FatherPage):
    # 类的属性
    title = None

    # 类的方法
    def __init__(self, master: Tk):
        super().__init__(master)
        self.master = master
        # 初始化框架
        super().create_top_frame(self.title)
        super().create_seq()
        self.__content_frame = Frame(self.master, bg="white", width=600, height=300)
        self.__tips_frame = LabelFrame(self.master, text="提示", labelanchor="n", font=("微软雅黑", 12),
                                       bg="white", width=190, height=290)
        self.__under_frame = Frame(self.master, bg="white", width=800, height=100)

    # 内容框架
    def create_content_frame(self):
        self.__content_frame.place(x=0, y=51)

    # 提示框架
    def create_tips_frame(self):
        self.__tips_frame.place(x=600, y=51)

    # 返回按钮框架
    def create_under_frame(self):
        self.__under_frame.place(x=0, y=350)


if __name__ == '__main__':
    root = Tk()
    root.title("内容页测试")
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
    content_page = ContentPage(root)
    content_page.create_content_frame()
    content_page.create_tips_frame()
    content_page.create_under_frame()
    root.mainloop()