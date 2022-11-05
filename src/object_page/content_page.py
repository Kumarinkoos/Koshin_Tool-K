"""
内容页父类，用于给具体的页面继承
继承于father page，给各具体内容页继承
框架主要包括顶部标签用框架、内容框架、提示框架、返回框架
由于页面父类已经定义好了标签框架和分割线，所以只需要给title就可以进行初始化
但作为内容页的父类，title给了None，具体的给内容页继承重写，这里只做一个传递
内容页父类定义了：
    内容框架（content_frame）因为要给子类使用这个框架，所以没有私有化
    提示框架（__tips_frame）区别于菜单的提示，大小不一样，
    所有内容页都有提示框架，所以私有化，并初始化好了，子类只需要给出tips_txt即可
    底部框架（under_frame）因为要给子类使用这个框架，所以没有私有化
    提示标签（__content_tips_label）因为主要重写tips_txt就可以完成对提示标签的初始化，
    所以这个标签页进行了私有化。
    初始化了各类跳转按钮，并没有放置他们，具体放置（jump_button_in_under_frame）需要在子类中重写
    设定了返回主菜单按钮的功能，所有子类的返回主菜单的按钮都指向主菜单
    设定了销毁页面的功能，内容页子类都统一了的4个框架加1个分割线，所以在内容页父类中直接定义该方法

    肯定需要重写的方法：
        func_in_content_frame：子类要有功能需要将这个方法重写，并把功能放在这个方法里
        jump_button_in_under_frame：子类要有跳转按钮需要将这个方法重写，跳转按钮需要布局放在这个方法中

    可以选择重写的方法：
        __next_page：下一步的方法，有下一步跳转的需要重写这个方法
        __back_page：上一步的方法，有上一步跳转的需要重写这个方法
        __finish_page：完成的方法，有最后完成的需要重写这个方法
@ author: Kumarinko
@ version: 1.0.0
@ date: 2022-11-04
"""
# 这里不能使用导入from src.menu_page import menu_page的引用语句，会出现循环引用的报错、
from tkinter import *
from src.object_page import father_page


class ContentPage(father_page.FatherPage):
    # 类的属性
    title = None
    tips_txt = None
    # 跳转按钮文字
    __return_button_txt = "返回主菜单"
    __next_button_txt = "下一步"
    __back_button_txt = "上一步"
    __finish_button_txt = "完成"

    # 类的方法
    def __init__(self, master: Tk):
        super().__init__(master)
        self.master = master
        # 初始化框架
        # 初始化标签框架（top_frame）和分割线同时设置标题
        super().title_label_in_top_frame(self.title)
        # 初始化内容框架（content_frame）
        self.content_frame = Frame(self.master, bg="white", width=600, height=300)
        self.content_frame.place(x=0, y=51)
        # 初始化提示框架（tips_frame）
        self.__tips_frame = LabelFrame(self.master, text="提示", labelanchor="n", font=("微软雅黑", 12),
                                       bg="white", width=190, height=290)
        self.__tips_frame.place(x=600, y=51)
        # 初始化跳转框架（under_frame）
        self.under_frame = Frame(self.master, bg="white", width=800, height=100)
        self.under_frame.place(x=0, y=350)
        # 初始化提示文本
        self.__content_tips_label = Label(self.__tips_frame, text=self.tips_txt, bg="white")
        self.__content_tips_label.place(x=0, y=0)
        # 初始化跳转按钮
        self.return_button = Button(self.under_frame, text=self.__return_button_txt, width=10, height=2,
                                    font=("微软雅黑", 12), bg="#89CFF0", command=self.__return_menu)
        self.next_button = Button(self.under_frame, text=self.__next_button_txt, width=10, height=2,
                                  font=("微软雅黑", 12), bg="#89CFF0", command=self.__next_page)
        self.back_button = Button(self.under_frame, text=self.__back_button_txt, width=10, height=2,
                                  font=("微软雅黑", 12), bg="#89CFF0", command=self.__back_page)
        self.finish_button = Button(self.under_frame, text=self.__finish_button_txt, width=10, height=2,
                                    font=("微软雅黑", 12), bg="#89CFF0", command=self.__finish_page)

    # 内容框架用于子类重写
    def func_in_content_frame(self):
        pass

    # 返回按钮框架用于子类重写
    def jump_button_in_under_frame(self):
        pass

    # 返回主菜单按钮用于子类重写避免循环引用
    def __return_menu(self):
        pass

    # 下一步按钮用于子类重写
    def __next_page(self):
        pass

    # 上一步按钮用于子类重写
    def __back_page(self):
        pass

    # 完成按钮用于子类重写
    def __finish_page(self):
        pass

    # 销毁页面
    def destroy_content_page(self):
        super().destroy_page()
        self.content_frame.destroy()
        self.under_frame.destroy()
        self.__tips_frame.destroy()


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
    content_page.func_in_content_frame()
    content_page.jump_button_in_under_frame()
    root.mainloop()
