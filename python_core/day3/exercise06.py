#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/25 15:30
# @Author   : SLNotFound
# @File     : exercise01.py

"""
在终端中输入一个年份，如果是闰年为变量day赋值29,否则赋值28。
 闰年条件：年份能被4整除但是不能被100整除，或者年份能被400整除
效果：
 请输入年份:2020
2020年的2月有29天
"""

year = int(input("请输入年份："))

day = 29 if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) else 28

print("%s年的2月有%s天" % (str(year), str(day)))
