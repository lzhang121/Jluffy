# -*- coding: utf-8 -*-
"""
@Name:        tmp_ex4.py
@Describe:    XXX
@Time:        2025/01/20 09:06:52
@Author:      Ray
@Version:     1.0
"""
import ast
import operator
from sympy import sympify


def expression_usage():
    # expression用法eval
    expression = "2 + 3 * (4 - 1)"
    print(eval(expression))


def literal_eval():
    # literal_eval 用法,不支持复杂运算
    expression = "[3, 4]"
    result = ast.literal_eval(expression)
    print(result)


def eval_control():
    allowed_globals = {"__builtins__": None}
    allowed_locals = {"x": 10, "y": 20}
    expression = "x + y * 2"
    result = eval(expression, allowed_globals, allowed_locals)
    print(result)  # 输出: 50


def sympy_expression():
    expression = "2 + 3 * (4 - 1)"
    print(sympify(expression))


def operator_expression(expression):
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    # expression = input("请输入两个数运算表达式(例如: 3 * 5):")
    # inputs = expression.split()

    tokens = expression.split()
    total = float(tokens[0])
    for i in range(1, len(tokens), 2):
        op, num = tokens[i], float(tokens[i+1])
        total = ops[op](total, num)
    return total


def main():
    # expression_usage()
    # literal_eval()
    # eval_control()
    # sympy_expression()
    # expression = "10 + 20 * 3 - 5"
    # result = operator_expression(expression)
    # print(result)
    sympy_expression()


if __name__ == '__main__':
    main()
