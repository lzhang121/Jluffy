# -*- coding: utf-8 -*-
"""
@Name:        ex3.py
@Describe:    XXX
@Time:        2025/01/13 20:50:49
@Author:      Ray
@Version:     1.0
"""
import random


def main():
    poke_types = ('❤️', '♣️', '♦️', '♠️')
    poke_values = ('2', '3', '4', '5', '6', '7',
                   '8', '9', '10', 'L', 'Q', 'K', 'A')

    print(random.choice(poke_types)+random.choice(poke_values))
    poke = []
    for poke_type in poke_types:
        for poke_value in poke_values:
            poke.append(poke_type+poke_value)

    print(poke)
    A1 = random.sample(poke, 3)
    for item in A1:
        poke.remove(item)
    A2 = random.sample(poke, 3)
    for item in A2:
        poke.remove(item)
    A3 = random.sample(poke, 3)
    print(A1)
    print(A2)
    print(A3)

    a = [1, 2, 3]
    print(id(a), a)
    print(id(a[2]), a[2])
    a[2] = 300
    print(id(a), a)
    print(id(a[2]), a[2])
    print(id(a[0]), a[0])
    a = [4, 5, 6]
    print(id(a), a)
    print(id(a[0]), a[0])

    l1 = [1, 2, 3]
    l2 = [l1, 4, 5]
    print(id(l1), l1)
    print(id(l2[0]), l2)
    l2[0].append(4)
    print(id(l1), l1)
    print(id(l2[0]), l2)
    l2[0][2] = 300
    print(id(l1), l1)
    print(id(l2[0]), l2)
    # l1 = 200
    # print(id(l1), l1)
    # print(id(l2[0]), l2)

    # l2[0] = 200
    # print(id(l1), l1)
    # print(id(l2[0]), l2)

    l2[0] = 200
    l1[2] = 1000
    print(id(l1), l1)
    print(id(l2[0]), l2)

    l1 = [1, 2, 3, 4, 5]
    l2 = l1[:]
    print(id(l1), id(l1[0]), id(l1[1]), id(l1[2]), id(l1[3]))
    print(id(l2), id(l2[0]), id(l2[1]), id(l2[2]), id(l2[3]))
    # l3 = list(l1)
    # print(id(l3))
    # l4 = l1.copy()
    # print(id(l4))
    l1[1] = 20
    print(id(l1), id(l1[0]), id(l1[1]), id(l1[2]), id(l1[3]))
    print(id(l2), id(l2[0]), id(l2[1]), id(l2[2]), id(l2[3]))
    print(l1)
    print(l2)
    # print(l3)
    # print(l4)

    print(id(l1[0]))
    print(id(l2[0]))

    l1 = [4, 5]
    l2 = [1, 2, 3, l1]
    l3 = l2[:]
    l1[0] = 40
    print(l2)
    print(l3)


if __name__ == "__main__":
    main()
