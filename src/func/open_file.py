"""
打开文件的功能实现
打开文件夹建议使用explorer，
不要使用start，使用start的话，如果文件夹路径中有特殊符号就会打不开。
@ author: Kumarinko
@ version: 1.0.0
@ date: 2022-11-05
"""
import os


def open_file(file_path: str):
    os.system(f'explorer {file_path}')