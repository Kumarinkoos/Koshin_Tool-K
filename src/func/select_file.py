from tkinter import filedialog


def select_file():
    # 使用askopenfilename函数选择单个文件
    selected_file_path = filedialog.askopenfilename()
    return selected_file_path