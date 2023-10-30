#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
生成5 -- 20之间的数字平方
[25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
"""
count_list = []
for i in range(5, 20):
    count_list.append(i ** 2)

count_list1 = [item ** 2 for item in range(5, 20)]
print(count_list)
print(count_list1)
