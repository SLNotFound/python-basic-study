#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
向以上三个列表追加数据第4行数据
在第1个位置插入第5行数据
"""

city_list = ["香港", "云南", "广东"]
add_list = [7, 2, 1]
now_list = [171, 68, 40]

city_list.append("上海")
add_list.append(2)
now_list.append(37)
print(city_list)
print(add_list)
print(now_list)

city_list.insert(0, "台湾")
add_list.insert(0, 2)
now_list.insert(0, 36)
print(city_list)
print(add_list)
print(now_list)
