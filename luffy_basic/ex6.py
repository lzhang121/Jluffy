# -*- coding: utf-8 -*-
"""
@Name:        ex6.py
@Describe:    XXX
@Time:        2025/01/18 08:29:33
@Author:      Ray
@Version:     1.0
"""


def poke():
    poke_type = ["❤️", "♦️", "♣️", "♦️"]
    poke_num = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "L", "Q", "K"]
    for type in poke_type:
        for num in poke_num:
            print(f"{type}{num}", sep='\t', end='')

        print()


def arguments(name, sex='女', age='9'):
    print(f"name: {name}, sex: {sex}, age: {age}")


def argument_1(start, end=None):
    # 位置变量
    if end is None:
        print(f"start: {start}")
    else:
        print(f"start: {start}, end: {end}")


def argument_2(start, end):
    print(f"start: {start}, end: {end}")


def show_info(name, age, height=None, weight=None):
    print("*" * 20)
    print(f"name: {name}")
    print(f"age: {age}")
    if height:
        print(f"(Sa: {height}) ")
    if weight:
        print(f"[体重:{weight}]")
    print("*"*20)


def argument_3(args):
    print(f"type(args): {type(args)},args:{args}")


def argument_4(*args):
    print(f"type(args): {type(args)},args:{args}")


def print_info(**kargs):
    for key, value in kargs.items():
        print(f"key:{key}  value:{value}")


def print_info_2(name, age, sex):
    print(f"name: {name}")
    print(f"sex: {sex}")
    print(f"age: {age}")


def print_info_3(a, b, c, *args, **kargs):
    print(f"a:{a}")
    print(f"b:{b}")
    print(f"c:{c}")
    print(f"args:{args}")
    print(f"kargs:{kargs}")


def print_info_4(a, *b, **c):
    print(a)
    print(b)
    print(c)


def main():
    # for i in range(4):
    #     print("*"*30)
    #     poke()
    # print("*"*30)
    # arguments("ray", "F", "32")
    # argument_1("END")
    # argument_1("START", "END")

    # 关键字变量
    # argument_2(start=4, end=5)
    # argument_2(end=4, start=5)
    # argument_2(start=3, end=1)
    # show_info(name="rain", age=23, weight=70)
    # argument_3(1)
    # argument_4(1, 2, 3, 4, 5)
    # argument_3([1, 2, 3])
    # argument_4([1, 2, 3])
    # print(1, 2, 3, 4, sep='|', end="")
    # dict_1 = {"name": "ray", "sex": "F", "age": 34}
    # print_info(**dict_1)
    # print_info(name="ray", age=34, sex="F")
    # print_info_2(name="ray", age=34, sex="F")
    # print_info_3(1, 2, 3, 4, 5, 6, x=4, y=3)
    print_info_4(1, 2, 3, 4, 5, x=1, y=2, z=3)


if __name__ == '__main__':
    main()
