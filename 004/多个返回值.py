#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/6/28 9:14
# @Author   : SLNotFound
# @File     : 多个返回值.py

def sum_and_svg(list):
    sum = 0
    count = 0
    for e in list:
        if isinstance(e, int) or isinstance(e, float):
            count += 1
            sum += e
    return sum, sum / count


my_list = [20, 12, 2.8, 'a', 35, 5.9, -1.8]
tp = sum_and_svg(my_list)
print(tp)
