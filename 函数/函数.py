#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/6/28 8:53
# @Author   : SLNotFound
# @File     : 函数.py

def my_max(x, y):
    z = x if x > y else y
    return z


def say_hi(name):
    print("===正在执行say_hai()函数===")
    return name + ", 您好！"


a = 6
b = 9


result = my_max(a, b)
print(result)
print(say_hi("Alice"))
help(my_max)
print(my_max.__doc__)
