#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
二维列表
"""

list01 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]
# for item in list01[0]:
#     print(item)
#
# list02 = list01[1][::-1]
# for item in list02:
#     print(item)
#
# for i in range(0, 3):
#     print(list01[i][2])

for item in list01[::-1]:
    print(item[3])

for items in list01:
    for item in items:
        print(item, end=" ")
    print()
