#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
请输入整数:5
$$$$$
$ $
$ $
$ $
$$$$$
"""
num = int(input("请输入整数："))
print("$" * num)
i = 1
while i < num - 1:
    print("$" + " " * (num - 2) + "$")
    i += 1
print("$" * num)
