# -*- coding: utf-8 -*-
"""
@Name:        ex2.py
@Describe:    XXX
@Time:        2025/01/13 09:33:40
@Author:      Ray
@Version:     1.0
"""


def main():
    # 字符串打印
    text = """
        学生信息如下：
        姓名：%s
        性别：%s
        年级：%s
    """ % ("Ray", "男", "5")
    print(text)

    # 字符串左、右、居中对齐
    name, sex, age = "Ray", "男", "15"
    text_1 = f"姓名：{name:<15} 性别：{sex:>4} 年级：{age:^2}"
    print(text_1)
    name, sex, age = "Raymode", "男", "05"
    text_2 = "姓名：{:<15} 性别：{:>4} 年级：{:^2}".format(name, sex, age)
    print(text_2)

    # # 字符串切片
    # s = "I love spider"
    # print(s[::-1])
    # print(s[::2])
    # print(s[::-2])

    if __name__ == '__main__':
        print("===")
        # main()
        print("===")
