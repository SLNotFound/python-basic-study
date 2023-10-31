#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
对数字列表进行升序排列（小 --> 大）
"""

num_list = [1, 3, 4, 2, 5, 6, 7, 8, 9]

for i in range(len(num_list) - 1):
    for j in range(i + 1, len(num_list)):
        if num_list[i] > num_list[j]:
            num_list[i], num_list[j] = num_list[j], num_list[i]

print(num_list)
