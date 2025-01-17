# -*- coding: utf-8 -*-
"""
@Name:        ex2.py
@Describe:    XXX
@Time:        2025/01/12 08:28:58
@Author:      Ray
@Version:     1.0
"""
import os
import tempfile
import shutil


def exchange(file_path, replacements, out_path):
    try:
        # 读取原始文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 替换文件中的字符串
        for old, new in replacements.items():
            content = content.replace(old, new)

        # 使用临时文件来确保原子写入(避免在写入过程中因为程序崩溃导致数据丢失或不完整)
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as temp_file:
            temp_file.write(content)

        # 获取临时文件名
        temp_filename = temp_file.name

        # 替换原文件
        shutil.move(temp_filename, out_path)

        print('文件内容替换完成。')

    except FileNotFoundError:
        print(f"文件 {file_path} 未找到，请检查路径是否正确。")
    except IOError as e:
        print(f"发生IO错误: {e}")
    except Exception as e:
        print(f"发生未知错误: {e}")
    finally:
        # 清理可能存在的临时文件
        if 'temp_filename' in locals() and os.path.exists(temp_filename):
            os.remove(temp_filename)


def main():
    replacements = {
        'ordezez': '张三',
        'supplier': '李四',
        'date': '20240911'
        # 可以添加更多的替换对
    }
    file_path = 'luffy_basic/inputs/t.txt'
    out_path = 'luffy_basic/outputs/report.txt'
    exchange(file_path, replacements, out_path)


if __name__ == '__main__':
    main()
