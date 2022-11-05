"""
找寻文件模板界面，用于找寻各类文件的模板
继承于content page
框架主要包括顶部标签用框架、内容框架、提示框架、返回框架
重写了内容框架里的功能（func_in_content_frame）
重写了跳转框架里的功能（jump_button_in_under_frame），添加了返回按钮
功能要求：
    用Listbox设置可选择的文件列表
    按钮1为打开所选文件所在文件夹
    按钮2为将所选文件复制到桌面
@ author: Kumarinko
@ version: 1.0.0
@ date: 2022-11-04
"""
from tkinter import *
from tkinter import messagebox
from src.object_page import content_page
from src.menu_page import menu_page
from src.func import open_file_in_folder
from src.func import copy_file_to_desktop
# 测试用
import test


class FindPage(content_page.ContentPage):
    # 类的属性
    title = "找寻文件模板"
    tips_txt = "找寻文件模板"
    __return_button_txt = "返回主菜单"
    find_label_txt = "请选择要找的文件模板："
    check_label_txt = "被选择的文件为："
    check_button_txt = "确认选择文件"
    open_button_txt = "打开文件位置"
    copy_button_txt = "复制到桌面"
    __find_list_content = ["设计变更提案书", "项目评价一览表", "试验报告书-利天承认", "试验报告书-本社承认", "尺寸报表",
                           "部品图变更通知票", "组立图变更通知票", "PRONES变更通知票", "ONLINE判定表", "更新金型发注申请表",
                           "金型发注用确认书（注塑模）", "金型发注用确认书（吹塑模）", "更新金型结果报告", "成本降低提案书"]

    # 类的方法
    # 初始化框架
    def __init__(self, master: Tk):
        super().__init__(master)
        self.master = master
        self.return_button = Button(self.under_frame, text=self.__return_button_txt, width=10, height=2,
                                    font=("微软雅黑", 12), bg="#89CFF0", command=self.__return_menu)
        # 初始化内容框架的控件
        # 初始化选择文件列表标签
        self.find_list_label = Label(self.content_frame, text=self.find_label_txt, font=("微软雅黑", 14), bg="white")
        # 初始化滚动条
        self.find_list_scrollbar = Scrollbar(self.content_frame)
        # 初始化Listbox用来放查找文件的内容
        self.find_listbox = Listbox(self.content_frame, font=("微软雅黑", 12), height=11, width=24, bd=3,
                                    yscrollcommand=self.find_list_scrollbar.set)

        # 初始化确认标签
        self.check_label = Label(self.content_frame, text=self.check_label_txt, font=("微软雅黑", 12), bg="white", fg="red")
        # 初始化显示被选择的文件的文本，这个文本需要有个变量来接收选中的listbox的内容
        self.check_var = StringVar()
        self.check_entry = Entry(self.content_frame, bg="#B0B0B0", font=("微软雅黑", 14), width=25,
                                 textvariable=self.check_var)
        # 初始化按钮
        self.check_button = Button(self.content_frame, text=self.check_button_txt, width=12, height=2,
                                   font=("微软雅黑", 12), bg="#89CFF0", command=self.func_check_button)
        self.open_button = Button(self.content_frame, text=self.open_button_txt, width=12, height=2,
                                  font=("微软雅黑", 12), bg="#89CFF0", command=self.func_open_button)
        self.copy_button = Button(self.content_frame, text=self.copy_button_txt, width=12, height=2,
                                  font=("微软雅黑", 12), bg="#89CFF0", command=self.func_copy_button)

    # 对内容框架的方法重写
    def func_in_content_frame(self):
        # 放置各个组件
        self.find_list_label.place(x=40, y=10)
        self.find_listbox.place(x=40, y=40)
        self.find_list_scrollbar.place(x=260, y=40, height=250)
        self.find_list_scrollbar.config(command=self.find_listbox.yview)
        for item in self.__find_list_content:
            self.find_listbox.insert("end", item)

        self.check_label.place(x=300, y=15)
        self.check_entry.place(x=300, y=50)
        self.check_entry.config(state=DISABLED)
        self.check_button.place(x=370, y=100)
        self.open_button.place(x=370, y=170)
        self.copy_button.place(x=370, y=240)

    # 对跳转框架的方法重写
    def jump_button_in_under_frame(self):
        # 找寻文档模板中只有返回主菜单按钮
        self.return_button.place(x=40, y=15)

    # 内容框架的功能
    # 确认按钮的功能
    def func_check_button(self):
        try:
            get_listbox_val = self.find_listbox.get(self.find_listbox.curselection())
            # 设置标签的值
            self.check_var.set(get_listbox_val)
        except Exception as warning:
            messagebox.showwarning("警告信息", "没有选择任何条目")

    # 打开文件所在文件夹按钮的功能
    def func_open_button(self):
        get_entry_val = self.check_entry.get()
        if get_entry_val == "":
            messagebox.showwarning("警告信息", "没有选择任何条目")
        else:
            message = open_file_in_folder.open_file_in_folder(get_entry_val)
            if message == "未找到模板文件的目录，请联系部长或开发者":
                messagebox.showerror("错误信息", message)

    # 打开复制到桌面的按钮
    def func_copy_button(self):
        get_entry_val = self.check_entry.get()
        if get_entry_val == "":
            messagebox.showwarning("警告信息", "没有选择任何条目")
        else:
            message = copy_file_to_desktop.copy_file_to_desktop(get_entry_val)
            if message == "未找到模板文件，请联系部长或开发者":
                messagebox.showerror("错误信息", message)
            elif message == "桌面已有同名文件，请检查文件以免被覆盖":
                messagebox.showwarning("警告信息", message)
            else:
                message = "已复制到桌面"
                messagebox.showinfo("执行信息", message)

    # 子类重写返回主菜单
    def __return_menu(self):
        self.destroy_content_page()
        menu_p = menu_page.MenuPage(self.master)
        menu_p.button_in_button_frame()
        menu_p.tips_label_in_tips_frame()


if __name__ == '__main__':
    root = Tk()
    test.root_test(root, "找寻文件模板测试页")
    find_page = FindPage(root)
    find_page.func_in_content_frame()
    find_page.jump_button_in_under_frame()
    root.mainloop()
