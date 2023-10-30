#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
生成10--30之间能被3或者5整除的数字
[10, 12, 15, 18, 20, 21, 24, 25, 27]
"""
count_list = []
for i in range(10, 30):
    if i % 3 == 0 or i % 5 == 0:
        count_list.append(i)
count_list1 = [item for item in range(10, 30) if item % 3 == 0 or item % 5 == 0]
print(count_list)
print(count_list1)
