# -*- coding: utf-8 -*-
"""
@Name:        ex2.py
@Describe:    XXX
@Time:        2025/01/13 09:33:40
@Author:      Ray
@Version:     1.0
"""
import sys
import random


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

    # 字符串切片
    s = "I love spider"
    print(s)
    print(s[::-1])
    print(s[::2])
    print(s[::-2])
    print(s[:5])
    print(s[5:])
    print(s[5:0:-1])

    # 字符串包含
    t = "love"
    if t in s:
        print("string_s includes strint_t")
    else:
        print("string_s doesn't include strint_t")

    # 字符串函数
    # upper,lower,capitalize,startswith,endswith,replace,trip,is_capital,isupper,islower
    s = "love"
    print(s.upper())
    print(s.lower())
    print(s.capitalize())
    print(s.startswith('lo'))
    print(s.endswith('ve'))
    print(s.replace('ve', 'w'))
    print(s.isupper())
    print(s.islower())
    print(s.isdigit())
    print(s.strip())
    text = "  Hello, World!  "
    result = text.strip()
    print(result)  # 输出: "Hello, World!"
    print(text.find('o'))
    print(text.split('o'))
    print(text.count('o'))
    print(text.index('o'))
    print(text.rstrip())
    print(text.lstrip())
    print(text.replace("o", "O").replace("v", "V").replace("l", "L"))

    s = "hello world"
    print(s[-5:])
    print(s[-1:-6:-1])

    # expression = input("请输入两个数的运算: ")
    # s = input("请输入两个数相加: ")
    s = "4 + 2"
    nums = s.split("+")
    print(int(nums[0].strip())+int(nums[1].strip()))
    s = 13971992204
    s1 = str(s)[:4]+'*'+str(s)[5:7]+'*'+str(s)[8:]
    print(s1)

    # 字符串替换
    lpath = "/Users/zhanglei/git/Jluffy/ex1.py"
    dpath = lpath.replace("/", "\\")
    print(dpath)

    # 判断字符串是否回文abba abcba
    s = "aba"
    s = "abba"
    # s = "abcba"
    # s = "abcd"
    # leng = len(s) // 2

    # if s[0:leng] == s[:leng:-1]:
    #     print("是回文")
    # else:
    #     if s[0:leng] == s[:leng-1:-1]:
    #         print("是回文")
    #     else:
    #         print("不是回文")
    if s == s[::-1]:
        print("是回文")
    else:
        print("不是回文")

    for i in range(1, 10):
        for j in range(1, i+1):
            print("{} * {} = {:<2} ".format(j, i, i*j), end=' ')
        print()

    poke_types = ('♠️', '♣️', '♦️', '♠️')
    poke_values = ('1', '2', '3', '4', '5', '6', '7',
                   '8', '9', '10', 'L', 'Q', 'K', 'A')

    print(random.choice(poke_types)+random.choice(poke_values))
    poke = []
    for poke_type in poke_types:
        for poke_value in poke_values:
            poke.append(poke_type+poke_value)

    pokers = {'A': [], 'B': [], 'C': [], 'D': []}
    print(pokers)
    for key, _ in pokers.items():
        for i in range(14):
            tmp = random.choice(poke)
            pokers[key].append(tmp)
            poke.remove(tmp)
    for key, value in pokers.items():
        print(key, value)

    init_value = 10000
    init_rate = 1.0325
    year = 1
    while True:
        rates = pow(init_rate, year)
        values = init_value * rates
        if values >= 20000:
            print("经过{}年,利息大于本金, 总金额:{:.1f}".format(year, values))
            break
        year += 1

    n = 20
    if n < 2:
        print("斐波那契至少大于等于2元素")
        sys.exit(-1)
    for i in range(2, n+1):
        if i == 2:
            a, b = 0, 1
            print(a, b, end=' ')
        else:
            a, b = b, a+b
            print(b, end=' ')
    print()
    # count = 3
    # while count > 0:
    #     num = input("请输入一个【0,10】之间的数: ")
    #     if int(num) == 5:
    #         print("你猜对了")
    #         sys.exit(0)
    #     elif int(num) > 5:
    #         print("你猜大了")
    #     else:
    #         print("你猜小了")
    #     count -= 1
    # print("you're lost")

    # print("打印一个nxn矩阵，要求元素值等于行列之和")
    # n = int(input("请输入n: "))
    # if n == 1:
    #     print("矩阵至少等于2")
    #     sys.exit()
    # matrix = []
    # for i in range(1, n+1):
    #     matrix.append(list(map(str, list(range(i, i+n)))))
    # for item in matrix:
    #     row = ", ".join(item)
    #     print(row)

    a = [1, 2, 3]
    print("id(a):{},a:{}".format(id(a), a))
    b = [4, 5, 6]
    c = a + b
    a.extend(b)
    print("id(a):{},a:{}".format(id(a), a))
    print("id(b):{},b:{}".format(id(b), b))
    print("id(c):{},c:{}".format(id(c), c))
    a.insert(6, 7)
    print("id(a):{},a:{}".format(id(a), a))
    # pop返回元素值
    del_item = a.pop(6)
    print("删除的元素: ", del_item)
    print("id(a):{},a:{}".format(id(a), a))
    # 返回None
    rem_item = a.remove(6)
    print("remove返回值: ", rem_item)
    print("id(a):{},a:{}".format(id(a), a))
    print("删除值: ", a[0])
    # 从内存中删除
    del a[0]
    print("id(a):{},a:{}".format(id(a), a))
    a.insert(5, 0)
    a1 = sorted(a, reverse=False)
    print("id(a):{},a:{}".format(id(a), a))
    print("id(a1):{},a1:{}".format(id(a1), a1))
    a2 = list(reversed(a))
    print("id(a):{},a:{}".format(id(a), a))
    print("id(a2):{},a2:{}".format(id(a2), a2))
    a.sort(reverse=False)
    print("id(a):{},a:{}".format(id(a), a))
    a.reverse()
    print("id(a):{},a:{}".format(id(a), a))
    print(a.index(2))
    print(a.count(2))
    a.clear()
    print("id(a):{},a:{}".format(id(a), a))


if __name__ == '__main__':
    main()
