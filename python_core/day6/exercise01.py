#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
根据月日,计算是这一年的第几天.
公式：前几个月总天数 + 当月天数
例如：5月10日
计算：31 29 31 30 + 10
"""
now_date = input("请输入今天的日期(格式为2023-01-01):")
day_tuple = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
date_list = now_date.split("-")
year, month, day = (int(item) for item in date_list)

if int(month) > 1:
    ret = 0
    if (year % 4 == 0 and year % 100 == 0) or year % 400 == 0:
        for item in day_tuple[0:month-1]:
            ret += item
        print("今天是%d年的第%d天" % (year, ret+day+1))
    else:
        for item in day_tuple[0:month-1]:
            ret += item
        print("今天是%d年的第%d天" % (year, ret+day))
else:
    print("今天是%d年的第%d天" % (year, day))
