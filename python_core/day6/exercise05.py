#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
在终端中打印香港字典的所有键(一行一个)
在终端中打印云南字典的所有值(一行一个)
在终端中打印广东字典的所有键和值(一行一个)
在广东字典中查找值是40对应的键名称
"""
hk_dict = {"add": 7, "now": 171, "sum": 11531, "cure": 11155, "death": 205}
yn_dict = {"add": 2, "now": 68, "sum": 301, "cure": 231, "death": 2}
gd_dict = {"add": 1, "now": 40, "sum": 2290, "cure": 2242, "death": 8}

for key in hk_dict:
    print(key)

for value in yn_dict.values():
    print(value)

for key, value in gd_dict.items():
    print(key, value)

for key, value in gd_dict.items():
    if value == 40:
        print(key)
