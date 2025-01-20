# -*- coding: utf-8 -*-
"""
@Name:        ex7.py
@Describe:    XXX
@Time:        2025/01/18 19:03:16
@Author:      Ray
@Version:     1.0
"""
import sys
import math
import random
import string


def test_1():
    return 1


def test_2():
    pass


def test_3():
    data = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
    data.sort(key=lambda x: x[1], reverse=False)
    print(data)

    nums = [1, 2, 3, 4]
    nums_2 = [i*i for i in nums]
    print(nums_2)
    nums_3 = list(map(lambda x: x*x, nums))
    print(nums_3)


def test_4():
    t = [3, 4, 5, 6]
    tt = dict(enumerate(t))
    print(tt)
    for key, value in enumerate(t, 4):
        print(key, value)


def flag(x):
    return x % 2 == 1


def test_5():
    t = [1, 2, 3, 4, 5, 6]
    tt = list(filter(flag, t))
    print(tt)


def recommand_hobby(re_set):
    peiQi_hobby = {'PA', 'PB', 'PC', 'PD'}
    alex_hobby = {'PA', 'PF', 'PG', 'PD'}
    yuan_hobby = {'PT', 'PB', 'PG', 'PD'}
    if re_set not in ("peiQi_hobby", "alex_hobby", "yuan_hobby"):
        print("输入错误没有此人")
        sys.exit()
    hobby_recommand = {}
    if re_set == "peiQi_hobby":
        hobby_recommand = alex_hobby.intersection(yuan_hobby)
    elif re_set == "alex_hobby":
        hobby_recommand = peiQi_hobby.intersection(yuan_hobby)
    else:
        hobby_recommand = peiQi_hobby.intersection(alex_hobby)
    return hobby_recommand


def recommand_hobby_1(name):
    hobby_dict = {
        "peiQi_hobby": {'PA', 'PB', 'PC', 'PD'},
        "alex_hobby": {'PA', 'PF', 'PG', 'PD'},
        "yuan_hobby": {'PT', 'PB', 'PG', 'PD'}
    }

    current_hobby_base = hobby_dict.pop(name)
    recommand_hobby = set()
    for key, value in hobby_dict.items():
        recommand = value - current_hobby_base
        if len(recommand) >= 1:
            recommand_hobby.update(recommand)
    return recommand_hobby


def foo_1(x):
    x[0] = 100
    x.append(4)
    print(x)


def circle(x):
    return math.pi * 2 * x, math.pi * x * x


def random_string(num):
    sample = string.ascii_letters + string.digits
    random_sample_string = "".join(random.choices(sample, k=num))
    return random_sample_string


def charpter_4_test():
    code = "sum([1*3+5,(5-9)*3,13*4-2])"
    l_code = eval(code)
    print(l_code)

    ll = [11, 22, 33, 44]
    ll_1 = list(x*x for x in ll)
    print(ll_1)

    ll_2 = ["apple", "banana", "cherry", "date"]
    ll_3 = list(filter(lambda x: len(x) <= 5, ll_2))
    print(ll_3)

    ll_4 = sorted(ll_2, key=lambda x: len(x), reverse=True)
    print(ll_4)

    student_dict = [
        {"name": "ray", "age": 23},
        {"name": "Ava", "age": 32},
        {"name": "amount", "age": 32},
        {"name": "raymode", "age": 32},
        {"name": "calivn", "age": 13}
    ]
    pick_up_dict_age = list(filter(lambda x: x["age"] > 20, student_dict))
    print(pick_up_dict_age)

    pick_up_dict_name = list(
        filter(lambda x: x["name"].startswith('A') or x["name"].startswith('a'), student_dict))
    print(pick_up_dict_name)

    pick_up_dict_name_v = list(
        filter(lambda x: x["name"].lower().startswith('a'), student_dict))
    print(pick_up_dict_name_v)


def triple_string(letter):
    return str(letter)*3


def main():
    # t1 = test_1()
    # t2 = test_2()
    # print(f"t1:{t1}")
    # print(f"t2:{t2}")
    # test_3()
    # test_4()
    # test_5()
    # print(recommand_hobby("peiQi_hobby"))
    # print(recommand_hobby("alex_hobby"))
    # print(recommand_hobby("yuan_hobby"))
    # print(recommand_hobby_1("yuan_hobby"))
    # l = [1, 2, 3]
    # foo_1(l)
    # print(l)
    # charpter_4_test()
    triple_string_var = triple_string('2')
    print(triple_string_var)


if __name__ == '__main__':
    main()

    # x = 10
    # # def my_func():
    # #     print(x)

    # def outer():
    #     x = 20
    #     def my_func():
    #         print(x)
    #     my_func()

    # outer()

    # perimeter, area = circle(4)
    # print(f"周长: {perimeter:.2f}, 面积: {area:.2f}")
    # print(random_string(30))
