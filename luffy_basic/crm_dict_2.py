# -*- coding: utf-8 -*-
"""
@Name:        CRM.py
@Describe:    XXX
@Time:        2025/01/16 23:03:00
@Author:      Ray
@Version:     1.0
"""
import sys


def num_name(num):
    if num == 1:
        name = "phone"
    elif num == 2:
        name = "battery"
    elif num == 3:
        name = "cable"
    elif num == 4:
        name = "laptop"
    elif num == 5:
        name = "printer"
    else:
        print("商品序列中么有该商品")
        sys.exit(-1)
    return name


def main():
    shopping_cart = {
        1000: {"name": "phone", "price": 25, "quantity": "1"},
        1001: {"name": "battery", "price": 30, "quantity": "2"},
        1002: {"name": "printer", "price": 35, "quantity": "3"}
    }

    while True:
        print("""
            --------------------------
            1. 添加商品
            2. 删除商品
            3. 修改商品
            4. 查询一个商品
            5. 查询所有商品
            6. 退出
            --------------------------
            """)
        choice = input("请输入你的选择:")

        if choice == "1":
            goods = """
            1. phone
            2. battery
            3. cable
            4. laptop
            5. printer
            """
            print(goods)
            num = int(input("请选择商品(1~5):"))
            name = num_name(num)
            price = input("请输入商品价格:")
            quantity = input("请输入商品等级:")
            key = list(shopping_cart.keys())[-1] + 1
            good = {"name": name, "price": price, "quantity": quantity}
            shopping_cart.update({key: good})
            print(f"添加客户{name}成功")

        if choice == "2":
            goods = """
            1. phone
            2. battery
            3. cable
            4. laptop
            5. printer
            """
            print(goods)
            num = int(input("请选择要删除的商品(1~5):"))
            name = num_name(num)

            flag = False
            for key, value in shopping_cart.items():
                if value["name"] == name:
                    shopping_cart.pop(key)
                    print(f"删除商品{name}成功")
                    flag = True
                    break
            if flag:
                print(f"没有找到名为{name}的商品")

        if choice == "3":
            goods = """
            1. phone
            2. battery
            3. cable
            4. laptop
            5. printer
            """
            print(goods)
            num = int(input("请选择要修改的商品(1~5):"))
            name = num_name(num)
            flag = False
            # for index in range(len(customers)):
            for key, value in shopping_cart.items():
                if value["name"] == name:
                    price = input("请输入商品价格:")
                    quantity = input("请输入商品等级:")
                    good = {"name": name, "price": price, "quantity": quantity}
                    shopping_cart.pop(key)
                    shopping_cart[key] = good
                    print(f"修改商品{name}成功")
                    flag = True
                    break

            if flag:
                print(f"没有找到名为{name}的商品")

        if choice == "4":
            goods = """
            1. phone
            2. battery
            3. cable
            4. laptop
            5. printer
            """
            print(goods)
            num = int(input("请输入要查询的商品(1~5):"))
            name = num_name(num)
            flag = False
            for key, value in shopping_cart.items():
                if value["name"] == name:
                    price, quantity = value["price"], value["quantity"]
                    print(f"商品:{name}, 价格:{price}, 等级:{quantity}")
                    flag = True
                    break
            if not flag:
                print(f"没有找到名为{name}的商品")

        if choice == "5":
            for key, value in shopping_cart.items():
                name = value["name"]
                price = value["price"]
                quantity = value["quantity"]
                print(f"商品:{name}, 价格:{price}, 等级:{quantity}")

        if choice == "6":
            sys.exit()


if __name__ == '__main__':
    main()
