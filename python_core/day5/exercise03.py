#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
在终端中,循环录入字符串,如果录入空则停止.
停止录入后打印所有内容(一个字符串)
"""
str_list = []
while True:
    str1 = input("请输入字符串：")
    if not str1:
        break
    else:
        str_list.append(str1)

print("".join(str_list))
