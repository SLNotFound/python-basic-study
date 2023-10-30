#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
删除香港现有人数信息
删除广东新增人数信息
删除云南的新增和现有信息
"""
hk_dict = {"add": 7, "now": 171, "sum": 11531, "cure": 11155, "death": 205}
yn_dict = {"add": 2, "now": 68, "sum": 301, "cure": 231, "death": 2}
gd_dict = {"add": 1, "now": 40, "sum": 2290, "cure": 2242, "death": 8}

del hk_dict["now"]
print(hk_dict)
del gd_dict["add"]
print(gd_dict)
del yn_dict["add"]
del yn_dict["now"]
print(yn_dict)