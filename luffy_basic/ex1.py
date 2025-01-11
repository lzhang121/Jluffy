# -*- coding: utf-8 -*-
"""
@Name:        ex.py
@Describe:    XXX
@Time:        2025/01/11 18:28:24
@Author:      Ray
@Version:     1.0
"""

import sys
import math
from decimal import Decimal

# 瑞年判断方法


def is_leap(year):
    if year != int(year):
        sys.exit(-1)
    if (year / 400 == year // 400) or ((year / 4 == year // 4) and (year / 100 != year // 100)):
        print("{} is leap".format(year))
    else:
        print("{} not is leap".format(year))


# 主函数声明


def main():
    # 变量赋值的实质
    x, y = 1, 2
    xy = x + y
    print("内存地址:{},名为x变量 = {}".format(id(x), x))
    print("内存地址:{},名为y变量 = {}".format(id(y), y))
    print("内存地址:{},名为xy变量 = {}".format(id(xy), xy))
    z = x
    print("内存地址:{},名为z变量 = {}".format(id(z), z))
    x = 4
    print("内存地址:{},名为x变量 = {}".format(id(x), x))
    print("内存地址:{},名为z变量 = {}".format(id(z), z))

    # 变量互换
    a, b = 1, 2
    print(a, id(a))
    print(b, id(b))
    b, a = a, b
    print(a, id(a))
    print(b, id(b))

    # 自加自减避免空间浪费
    a = 100
    print(a)
    a -= 10
    print(a)

    # 下划线变量命名
    user_name = "zhanglei"
    pass_wd = "qatest"
    print(user_name, pass_wd)

    # 浮点型
    a = 3.12
    b = 3.2
    print(a + b)
    print(round(a + b))
    c = Decimal(b) - Decimal(a)
    print(c)

    # 多值分割
    print("I", "want", "fly", sep="|")

    # 运算符
    a = 100
    b = 3
    print(a ** b)
    print(a // b)
    print(a / b)

    # 变量赋值
    a = 1
    b = a
    c = b
    a, d = c + 1, b + 2
    a += 1
    print(id(a), a)
    print(id(d), d)

    # # input
    # r = input("请输入圆的半径: ")
    # print("圆的半径为: ", r)
    # print("圆的面积为: ", math.pow(float(r), 2)*3.14)

    # 判断数字是否被13整除
    a = 1000
    if a / 13 == a // 13:
        print("%d可以被13整除" % a)
    else:
        print("%d不可被13整除" % a)

    years = [2000, 2040, 1980, 1981, 1982, 1983, 1984]
    for year in years:
        is_leap(year)


if __name__ == '__main__':
    main()
