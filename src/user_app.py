"""
图形界面入口，用于创建主窗口和基框架
@ author: Kumarinko
@ version: 1.0.0
@ date: 2022-11-04
"""
from tkinter import *
from src.menu_page import menu_page


class MainPage:
    def __init__(self, master: Tk):
        self.root = master
        self.root.title("开发工具箱(Powered By Kumarinko)--version 1.0.0")
        # 设置窗口大小
        width = 800
        height = 450
        scree_center_width = int((self.root.winfo_screenwidth() - width) / 2)
        scree_center_height = int((self.root.winfo_screenheight() - height) / 2)
        self.root.geometry(f"{width}x{height}+{scree_center_width}+{scree_center_height}")

        # 设置背景为颜色
        self.root.config(background="white")

        # 窗口不可放大
        self.root.resizable(False, False)


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.__create_widgets(self.master)

    @staticmethod
    def __create_widgets(master=None):
        menu = menu_page.MenuPage(master)
        menu.creat_button_frame()
        menu.creat_tips_frame()


def root_init():
    root = Tk()
    MainPage(root)
    app = Application(master=root)
    app.mainloop()


if __name__ == '__main__':
    root_init()
