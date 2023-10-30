#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
在终端中打印香港的现有人数
在终端中打印云南的新增和现有人数
广东新增人数增加1
"""
hk_dict = {"add": 7, "now": 171, "sum": 11531, "cure": 11155, "death": 205}
yn_dict = {"add": 2, "now": 68, "sum": 301, "cure": 231, "death": 2}
gd_dict = {"add": 1, "now": 40, "sum": 2290, "cure": 2242, "death": 8}

print(hk_dict["now"])
print(yn_dict["add"])
print(yn_dict["now"])
gd_dict["add"] += 1
print(gd_dict)
