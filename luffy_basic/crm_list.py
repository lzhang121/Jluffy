# -*- coding: utf-8 -*-
"""
@Name:        CRM.py
@Describe:    XXX
@Time:        2025/01/16 23:03:00
@Author:      Ray
@Version:     1.0
"""
import sys


def main():
    customers = [
        ["Alice", 25, "alice@example.com"],
        ["Bob", 30, "bob@example.com"],
        ["Charles", 35, "charles@example.com"]
    ]

    while True:
        print("""
            --------------------------
            1. 添加客户
            2. 删除客户
            3. 修改客户
            4. 查询一个客户
            5. 查询所有客户
            6. 退出
            --------------------------
            """)
        choice = input("请输入你的选择:")

        if choice == "1":
            name = input("请输入添加客户的姓名:")
            age = input("请输入添加客户的年龄:")
            email = input("请输入添加客户的邮箱:")
            new_customer = [name, age, email]
            customers.append(new_customer)
            print(f"添加客户{name}成功")

        if choice == "2":
            name = input("请输入要删除客户的姓名:")
            flag = False
            for index in range(len(customers)):
                if customers[index][0] == name:
                    customers.pop(index)
                    print(f"删除客户{name}成功")
                    flag = True
                    break
            if flag:
                print(f"没有找到名为{name}的客户")

        if choice == "3":
            name = input("请输入要修改的客户姓名:")
            flag = False
            for index in range(len(customers)):
                if customers[index][0] == name:
                    age = input("请输入要修改的客户年龄:")
                    email = input("请输入要修改的客户邮箱:")
                    customers[index] = [name, age, email]
                    print(f"修改客户{name}成功")
                    flag = True
                    break

            if flag:
                print(f"没有找到名为{name}的客户")

        if choice == "4":
            name = input("请输入要查询客户的姓名:")
            flag = False
            for index in range(len(customers)):
                if customers[index][0] == name:
                    age, email = customers[index][1], customers[index][2]
                    print(f"用户:{name}, 年龄:{age}, email:{email}")
                    flag = True
                    break
            if not flag:
                print(f"没有找到名为{name}的客户")

        if choice == "5":
            for index in range(len(customers)):
                name = customers[index][0]
                age = customers[index][1]
                email = customers[index][2]
                print(f"用户:{name}, 年龄:{age}, email:{email}")

        if choice == "6":
            sys.exit()


if __name__ == '__main__':
    main()
