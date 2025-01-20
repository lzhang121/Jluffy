# -*- coding: utf-8 -*-
"""
@Name:        tmp_ex6.py
@Describe:    XXX
@Time:        2025/01/20 11:29:48
@Author:      Ray
@Version:     1.0
"""
import re
from collections import Counter

# 读取文档内容


def count_characters_in_file(file_path):
    try:
        # 打开文件并读取内容
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # 去掉空格和换行符，仅统计有效字符
        # text = text.replace("\n", "").replace(" ", "") #仅仅支持精确匹配
        text = re.sub(r'[\W|_]', '', text)

        # 使用 Counter 统计每个字的频率
        char_count = Counter(text)

        # 总字数
        total_chars = sum(char_count.values())

        # 输出统计结果
        print(f"文档总字数: {total_chars}")
        print("每个字出现的频率:")
        char_count_sorted = dict(
            sorted(char_count.items(), key=lambda item: item[1], reverse=True))
        top = 0
        for char, freq in char_count_sorted.items():
            top += 1
            if top <= 10:
                print(f"{char}: {freq}")
            else:
                break

        return char_count, total_chars

    except FileNotFoundError:
        print(f"文件 {file_path} 未找到，请检查路径。")
        return None


def main():
    file_path = "work_scene/inputs/test.txt"
    count_characters_in_file(file_path)


if __name__ == '__main__':
    main()
