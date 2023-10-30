#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
在地区列表中删除“香港”
在新增列表中删除第1个元素
在现有列表中删除前2个元素
"""

city_list = ["香港", "云南", "广东"]
add_list = [7, 2, 1]
now_list = [171, 68, 40]

city_list.remove("香港")
print(city_list)

del add_list[0]
print(add_list)

now_list = now_list[2:]
print(now_list)
