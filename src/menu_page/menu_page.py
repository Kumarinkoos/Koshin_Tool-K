"""
菜单页面，用于选择各个功能
继承于father page，不被其他页面继承
框架主要包括顶部标签用框架、按钮框架、提示框架
@ author: Kumarinko
@ version: 1.0.0
@ date: 2022-11-04
"""
from tkinter import *
from src.object_page import father_page
from src.help_page import help_page


class MenuPage(father_page.FatherPage):
    # 类的属性
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
        super().create_label_frame("菜单")
        super().create_seq()
        self.__button_frame = Frame(self.master, bg="white", width=600, height=400)
        self.__tips_frame = LabelFrame(self.master, text="提示", labelanchor="n", font=("微软雅黑", 12),
                                       bg="white", width=190, height=380)
        # 初始化按钮
        self.find_button = Button(self.__button_frame, text=self.__find_button_txt, width=10, height=2,
                                  font=("微软雅黑", 18), bg="#89CFF0", command=self.__change_find_page)
        self.report_button = Button(self.__button_frame, text=self.__report_button_txt, width=10, height=2,
                                    font=("微软雅黑", 18), bg="#89CFF0", command=self.__change_report_page)
        self.help_button = Button(self.__button_frame, text=self.__help_button_txt, width=10, height=2,
                                  font=("微软雅黑", 18), bg="#89CFF0", command=self.__change_help_page)
        # 初始化提示文本
        self.__label_find = Label(self.__tips_frame, text=self.__find_text, bg="white")
        self.__label_report = Label(self.__tips_frame, text=self.__report_text, bg="white")
        self.__label_help = Label(self.__tips_frame, text=self.__help_text, bg="white")

    # 按钮框架
    def creat_button_frame(self):
        # 按钮框架放置
        self.__button_frame.place(x=0, y=51)
        # 按钮放置
        # 找寻文件模板按钮
        self.find_button.grid(row=0, column=0, padx=20, pady=15)
        self.find_button.bind("<Enter>", func=self.__find_mouse_in)
        self.find_button.bind("<Leave>", func=self.__find_mouse_out)
        # 试验报告书按钮
        self.report_button.grid(row=0, column=1, padx=20, pady=15)
        self.report_button.bind("<Enter>", func=self.__report_mouse_in)
        self.report_button.bind("<Leave>", func=self.__report_mouse_out)
        # 帮助文档按钮
        self.help_button.grid(row=0, column=2, padx=20, pady=15)
        self.help_button.bind("<Enter>", func=self.__help_mouse_in)
        self.help_button.bind("<Leave>", func=self.__help_mouse_out)

    # 提示框架
    def creat_tips_frame(self):
        # 提示框架放置
        self.__tips_frame.place(x=600, y=51)
        # 提示框内鼠标不在按钮上为隐藏
        self.__label_find.place_forget()
        self.__label_report.place_forget()
        self.__label_help.place_forget()

    # 鼠标进出事件
    def __find_mouse_in(self, event):
        self.__label_find.place(x=0, y=0)

    def __find_mouse_out(self, event):
        self.__label_find.place_forget()

    def __report_mouse_in(self, event):
        self.__label_report.place(x=0, y=0)

    def __report_mouse_out(self, event):
        self.__label_report.place_forget()

    def __help_mouse_in(self, event):
        self.__label_help.place(x=0, y=0)

    def __help_mouse_out(self, event):
        self.__label_help.place_forget()

    # 鼠标点击换页
    def __change_find_page(self):
        pass

    def __change_report_page(self):
        pass

    def __change_help_page(self):
        self.__destroy_page()
        help_p = help_page.HelpPage(self.master)
        help_p.create_cut()
        help_p.create_return_button()

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
    menu_page.creat_button_frame()
    menu_page.creat_tips_frame()
    root.mainloop()
