# -*- coding: utf-8 -*-
"""
@Name:        tmp_ex5.py
@Describe:    XXX
@Time:        2025/01/20 10:04:29
@Author:      Ray
@Version:     1.0
"""
import os
import glob


def merge_txt_file(source_folder, dest_file):
    # 获取对应文件列表
    file_list = glob.glob(source_folder)
    current_dir = os.getcwd() + '/' + source_folder.partition("*")[0]

    # 如果找不到文件报错退出
    if len(file_list) == 0:
        raise FileNotFoundError(f"文件夹 {current_dir}")
    file_list.sort(reverse=False)

    # 遍历每个文件，逐行读取内容写入对应目标文件
    with open(dest_file, 'w') as wf:
        for file in file_list:
            with open(file, 'r') as rf:
                line = rf.readline()
                wf.write(line)
    return


def main():
    source_folder = "work_scene/inputs/*.txt"
    dest_file = "work_scene/outputs/merge_file.txt"
    merge_txt_file(source_folder, dest_file)


if __name__ == '__main__':
    main()
