#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
在终端中录入一个内容,循环打印每个文字的编码值。
效果：
请输入文字：qtx
113
116
120
"""
test_str = input("请输入文字：")
for item in test_str:
    print(ord(item))
