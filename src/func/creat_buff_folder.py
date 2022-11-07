"""
试验报告书步骤1中，按下上传表纸，将会新建一个buff文件，
之后的资料都会传到这个文件中来
@ author: Kumarinko
@ version: 1.0.0
@ date: 2022-11-07
"""
import os


def create_buff_folder():
    user_name_path = os.path.expanduser("~")
    desktop_path = os.path.join(user_name_path, "Desktop")
    os.mkdir(desktop_path + "\\buff")