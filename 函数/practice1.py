#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/6/29 16:25
# @Author   : SLNotFound
# @File     : practice1.py

"""
计算形如2+22+222+22+2的值
此时 a为2,n为3
"""


def cal(num, n):
    result = 0
    for i in range(n):
        result += num * 10 ** i
    return result


print(cal(1, 3))
