"""
选择文件的功能实现
@ author: Kumarinko
@ version: 1.0.0
@ date: 2022-11-05
"""
from tkinter import filedialog


def select_file():
    # 使用askopenfilename函数选择单个文件
    selected_file_path = filedialog.askopenfilename()
    new_selected_file_path = selected_file_path.replace("/", "\\")
    return new_selected_file_path
