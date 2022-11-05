"""
将选定的文件复制到桌面

*在文件被占用的时候，复制会出现问题，
提示PermissionError: [Errno 13] Permission denied
意为权限错误。
由于目前不知道该如何捕获这个Error（尝试了shutil.Error能捕获但不处理）
能力有限，使用另辟蹊径的方法
@ author: Kumarinko
@ version: 1.0.0
@ date: 2022-11-05
"""
import os
import shutil


def can_i_copy(src_path: str, desk_path: str, maybe_file: str):
    # 判断源文件是否存在
    if os.path.exists(src_path):
        # 判断目标文件夹是否已有同名文件
        if os.path.exists(maybe_file):
            message = "桌面已有同名文件，请检查文件以免被覆盖"
            return message
        else:
            shutil.copy(src_path, desk_path)
            message = "已复制到桌面"
            return message
    else:
        message = "未找到模板文件，请联系部长或开发者"
        return message


def copy_file_to_desktop(file_name: str):
    user_name_path = os.path.expanduser("~")
    desktop_path = os.path.join(user_name_path, "Desktop")
    if file_name == "设计变更提案书":
        src_file_path = "D:\\1-Work File\\Program\\Project-K\\K-file\\設計変更提案書.xlsx"
        # 由于没法捕捉权限错误的无奈之举
        maybe_file_in_desktop = desktop_path + "\\設計変更提案書.xlsx"
        message = can_i_copy(src_file_path, desktop_path, maybe_file_in_desktop)
        return message



if __name__ == '__main__':
    # 获取用户的目录
    print(os.path.expanduser('~'))
    # 将用户的目录和Desktop进行拼接，os.path.join会把用户目录和Desktop之间用\进行连接
    print(os.path.join(os.path.expanduser('~'), "Desktop"))
    src_file = "D:\\1-Work File\\Program\\Project-K\\K-file\\寸法検査表.xlsx"
    print(src_file)
