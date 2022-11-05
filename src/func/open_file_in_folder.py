"""
打开文件所在位置的功能实现
打开文件夹建议使用explorer，
不要使用start，使用start的话，如果文件夹路径中有特殊符号就会打不开。
@ author: Kumarinko
@ version: 1.0.0
@ date: 2022-11-05
"""
import os


def can_i_open(file_path: str):
    # 判断文件夹是否存在
    if os.path.exists(file_path):
        os.system(f'explorer /select, {file_path}')
        message = "已打开"
        return message
    else:
        message = "未找到模板文件的目录，请联系部长或开发者"
        return message


def open_file_in_folder(file_name: str):
    if file_name == "设计变更提案书":
        file_path = "D:\\1-Work File\\Program\\Project-K\\K-file\\設計変更提案書.xlsx"
        message = can_i_open(file_path)
        return message
    elif file_name == "项目评价一览表":
        pass
    elif file_name == "试验报告书-利天承认":
        pass
    elif file_name == "试验报告书-本社承认":
        pass
    elif file_name == "尺寸报表":
        pass
    elif file_name == "部品图变更通知票":
        pass
    elif file_name == "组立图变更通知票":
        pass
    elif file_name == "PRONES变更通知票":
        pass
    elif file_name == "ONLINE判定表":
        pass
    elif file_name == "更新金型发注申请表":
        pass
    elif file_name == "金型发注用确认书（注塑模）":
        pass
    elif file_name == "金型发注用确认书（吹塑模）":
        pass
    elif file_name == "更新金型结果报告":
        pass
    elif file_name == "成本降低提案书":
        pass


if __name__ == '__main__':
    dir_path = "D:\\1-Work File\\Program\\Project-K\\K-file"
    if os.path.exists(dir_path):
        os.system(f"explorer {dir_path}")
    else:
        print("有一个错误")
