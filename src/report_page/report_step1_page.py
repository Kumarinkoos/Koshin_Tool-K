"""
试验报告书步骤1界面，用于添加扫描表纸
继承于content page
框架主要包括顶部标签用框架、内容框架、提示框架、返回框架
重写了内容框架里的功能（func_in_content_frame）
重写了跳转框架里的功能（jump_button_in_under_frame），添加了返回按钮和下一步按钮
@ author: Kumarinko
@ version: 1.0.0
@ date: 2022-11-05
"""
from tkinter import *
from src.object_page import content_page
from src.menu_page import menu_page


class ReportStep1(content_page.ContentPage):
    # 类的属性
    title = "试验报告书步骤1"
    tips_txt = "试验报告书步骤1"
    __return_button_txt = "返回主菜单"
    __next_button_txt = "下一步"

    # 类的方法
    def __init__(self, master: Tk):
        super().__init__(master)
        self.master = master
        self.return_button = Button(self.under_frame, text=self.__return_button_txt, width=10, height=2,
                                    font=("微软雅黑", 12), bg="#89CFF0", command=self.__return_menu)
        self.next_button = Button(self.under_frame, text=self.__next_button_txt, width=10, height=2,
                                  font=("微软雅黑", 12), bg="#89CFF0", command=self.__next_page)

    # 子类重写内容框架里面写功能
    def func_in_content_frame(self):
        pass

    # 子类重写返回按钮框架里面放跳转按钮
    def jump_button_in_under_frame(self):
        self.return_button.place(x=40, y=15)
        self.next_button.place(x=650, y=15)

    # 子类重写返回主菜单
    def __return_menu(self):
        self.destroy_content_page()
        menu_p = menu_page.MenuPage(self.master)
        menu_p.button_in_button_frame()
        menu_p.tips_label_in_tips_frame()

    # 子类重写下一步
    def __next_page(self):
        pass


if __name__ == '__main__':
    root = Tk()
    root.title("找寻文件模板页测试")
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
    report_step1_page = ReportStep1(root)
    report_step1_page.func_in_content_frame()
    report_step1_page.jump_button_in_under_frame()
    root.mainloop()
