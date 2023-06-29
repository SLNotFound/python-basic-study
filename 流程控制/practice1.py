#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/6/29 15:51
# @Author   : SLNotFound
# @File     : practice1.py

"""
输入一个年份，判断是否是闰年。
闰年满足以下两个条件之一：
1、能被4整除，但不能被100整除
2、能被400整除
"""
input_year = input("请输入要判断是否为闰年的年份：")
check_year = int(input_year)
if (check_year % 4 == 0 and check_year % 100 != 0) or check_year % 400 == 0:
    print("%s 是闰年" % input_year)
else:
    print("%s 不是闰年" % input_year)
