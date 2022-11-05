"""
测试方法，用于单个页面在__name__ == '__main__'中测试使用
"""
from tkinter import *

def root_test(root:Tk,title: str):
    root.title(title)
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
