#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
 创建函数,在终端中打印矩形.
"""

number = int(input("请输入整数:"))  # 5


def print_rect(num):
    for row in range(num):
        if row == 0 or row == num - 1:
            print("*" * num)
        else:
            print("*" + " " * (num - 2) + "*")


print_rect(number)
