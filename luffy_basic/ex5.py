# -*- coding: utf-8 -*-
"""
@Name:        ex5.py
@Describe:    XXX
@Time:        2025\01\17 21:52:37
@Author:      Ray
@Version:     1.0
"""


def main():
    a1 = {1, 2, 3}
    a2 = {2, 3, 4}
    print(a1 & a2)
    print(a1 | a2)
    print(a1 - a2)

    dict_1 = {
        "a1": 8,
        "a2": 5,
        "a3": 4,
        "a4": 1,
        "a5": 12,
        "a6": 6
    }
    v = dict_1.get("a1")
    k = "a1"
    for key, value in dict_1.items():
        if v < value:
            v = value
            k = key
    print(k)

    vm = 1
    for key, value in dict_1.items():
        vm *= value
    print(vm)

    mlist = [1, 2, 3, 4, 5, 1, 2, 3, 7, 6]
    mset = set(mlist)
    mdict = {}
    for item in mlist:
        if item in mset:
            mdict[item] = mdict.get(item, 0) + 1

    print(mdict)

    students = [
        {"name": "ray1", "score": 40},
        {"name": "ray2", "score": 54},
        {"name": "ray3", "score": 34},
        {"name": "ray4", "score": 63},
        {"name": "ray5", "score": 32},
        {"name": "ray6", "score": 34},
        {"name": "ray7", "score": 23},
        {"name": "ray8", "score": 25},
        {"name": "ray9", "score": 80},

    ]

    name_list = [item.get("name") for item in students]
    print(len(set(name_list)))

    max_score, min_score = students[0]["score"], students[0]["score"]
    for item in students:
        if item["score"] > min_score:
            min_score = item["score"]
        if item["score"] < max_score:
            max_score = item["score"]
    print(max_score, min_score)

    students = {
        "Ray1": {"math": 90, "englist": 30, "history": 40},
        "Ray2": {"math": 90, "englist": 40, "history": 40},
        "Ray3": {"math": 90, "englist": 20, "history": 40},
        "Ray4": {"math": 90, "englist": 10, "history": 40},
        "Ray5": {"math": 90, "englist": 50, "history": 40},
    }

    for name, scores in students.items():
        total_score = sum(list(scores.values()))
        avg_score = total_score/len(list(scores.values()))
        print("student: {}, total_score: {} avg_score: {:.1f})".format(
            name, total_score, avg_score))


if __name__ == '__main__':
    main()
