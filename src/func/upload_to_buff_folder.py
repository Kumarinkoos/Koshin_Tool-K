"""
试验报告书步骤1中，按下上传表纸，将会新建一个buff文件，
之后的资料都会传到这个文件中来
@ author: Kumarinko
@ version: 1.0.0
@ date: 2022-11-07
"""
import os
import shutil


def upload_to_buff_folder(file_path):
    user_name_path = os.path.expanduser("~")
    desktop_path = os.path.join(user_name_path, "Desktop")
    folder_path = desktop_path + "\\buff"
    shutil.copy(file_path, folder_path)
