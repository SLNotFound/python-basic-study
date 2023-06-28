#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/6/28 9:16
# @Author   : SLNotFound
# @File     : 递归函数.py

def fn(n):
    if n == 0:
        return 1
    elif n == 1:
        return 4
    else:
        return 2 * fn(n-1) + fn(n-2)


print(fn(10))
