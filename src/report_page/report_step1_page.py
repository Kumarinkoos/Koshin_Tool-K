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
from src.report_page import report_step2_page
from src.func import select_file
# 测试用
import test


class ReportStep1(content_page.ContentPage):
    # 类的属性
    title = "试验报告书步骤1"
    tips_txt = "试验报告书步骤1"
    __return_button_txt = "返回主菜单"
    __next_button_txt = "下一步"
    upload_label_txt = "请选择要上传的表纸："
    select_label_txt = "被选择的文件为："
    select_button_txt = "选择文件"
    check_button_txt = "确认文件"
    upload_button_txt = "上传文件"

    # 类的方法
    def __init__(self, master: Tk):
        super().__init__(master)
        self.master = master
        self.return_button = Button(self.under_frame, text=self.__return_button_txt, width=10, height=2,
                                    font=("微软雅黑", 12), bg="#89CFF0", command=self.__return_menu)
        self.next_button = Button(self.under_frame, text=self.__next_button_txt, width=10, height=2,
                                  font=("微软雅黑", 12), bg="#89CFF0", command=self.__next_page)
        # 初始化内容框架的控件
        # 初始化选择文件的标签
        self.step1_upload_label = Label(self.content_frame, text=self.upload_label_txt, font=("微软雅黑", 14), bg="white",
                                        fg="red")
        # 初始化路径的文本
        self.file_path = StringVar()
        self.step1_path_entry = Entry(self.content_frame, bg="white", font=("微软雅黑", 10), width=70,
                                      textvariable=self.file_path)
        # 初始化被选择的文件显示标签
        self.step1_select_label = Label(self.content_frame, text=self.select_label_txt, font=("微软雅黑", 12), bg="white")
        self.select_file = StringVar()
        self.step1_select_entry = Entry(self.content_frame, bg="white", font=("微软雅黑", 14), width=25,
                                        textvariable=self.select_file)
        # 初始化按钮
        self.step1_select_button = Button(self.content_frame, text=self.select_button_txt, width=12, height=2,
                                          font=("微软雅黑", 12), bg="#89CFF0", command=self.func_select_button)
        self.step1_check_button = Button(self.content_frame, text=self.check_button_txt, width=12, height=2,
                                         font=("微软雅黑", 12), bg="#89CFF0", command=self.func_check_button)
        self.step1_upload_button = Button(self.content_frame, text=self.upload_button_txt, width=12, height=2,
                                          font=("微软雅黑", 12), bg="#89CFF0", command=self.func_upload_button)

    # 子类重写内容框架里面写功能
    def func_in_content_frame(self):
        self.step1_upload_label.place(x=20, y=20)
        self.step1_path_entry.place(x=20, y=50)
        self.step1_select_label.place(x=20, y=100)
        self.step1_select_entry.place(x=150, y=100)
        self.step1_select_button.place(x=440, y=90)
        self.step1_check_button.place(x=40, y=150)
        self.step1_upload_button.place(x=440, y=150)

    # 子类重写返回按钮框架里面放跳转按钮
    def jump_button_in_under_frame(self):
        self.return_button.place(x=40, y=15)
        self.next_button.place(x=650, y=15)

    # 内容框架的功能
    # 选择文件按钮
    def func_select_button(self):
        selected_file_path = select_file.select_file()
        self.file_path.set("")
        self.file_path.set(selected_file_path)
        path_list = selected_file_path.split("/")
        self.select_file.set("")
        self.select_file.set(path_list[-1])

    # 确认文件按钮
    def func_check_button(self):
        pass

    # 上传文件按钮
    def func_upload_button(self):
        pass

    # 子类重写返回主菜单
    def __return_menu(self):
        self.destroy_content_page()
        menu_p = menu_page.MenuPage(self.master)
        menu_p.button_in_button_frame()
        menu_p.tips_label_in_tips_frame()

    # 子类重写下一步
    def __next_page(self):
        self.destroy_content_page()
        report_step2_p = report_step2_page.ReportStep2(self.master)
        report_step2_p.func_in_content_frame()
        report_step2_p.jump_button_in_under_frame()


if __name__ == '__main__':
    root = Tk()
    test.root_test(root, "试验报告书步骤1测试页")
    report_step1_page = ReportStep1(root)
    report_step1_page.func_in_content_frame()
    report_step1_page.jump_button_in_under_frame()
    root.mainloop()
