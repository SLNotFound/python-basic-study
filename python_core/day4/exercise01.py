#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
练习：累加10 -- 60之间，个位不是3/5/8的整数和。
"""

sum_value = 0
for number in range(10, 61):
    unit = number % 10
    if unit == 3 or unit == 5 or unit == 8:
        # print(number)
        continue
    sum_value += number
print(sum_value)
