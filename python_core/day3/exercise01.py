#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/25 15:30
# @Author   : SLNotFound
# @File     : exercise01.py

"""
在终端中输入整数
打印正数、 负数、零

"""

num = input("请输入一个整数：")
if int(num) > 0:
    print("您输入的是正数")
elif int(num) == 0:
    print("您输入的是0")
else:
    print("您输入的是负数")
