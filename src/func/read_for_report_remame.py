"""
读取试验报告书（xlsx）的信息，由此组成最后的命名
@ author: Kumarinko
@ version: 1.0.0
@ date: 2022-11-06
"""
from openpyxl import *
from openpyxl.utils.exceptions import InvalidFileException

def read_excel_get_info(excel_file_path: str):
    try:
        # 尝试打开文件
        open_excel = load_workbook(excel_file_path)
    except InvalidFileException:
        # 打开的不是Excel
        message = "请选择xlsx文件"
        return message
    else:
        # 打开的是Excel
        pass