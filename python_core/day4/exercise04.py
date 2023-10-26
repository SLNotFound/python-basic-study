#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
练习：根据下列文字，提取变量，使用字符串格式化打印信息
湖北确诊67802人,治愈63326人,治愈率0.99
"""
num1 = 67802
num2 = 63326
rate = 0.99

print("湖北确诊%d人,治愈%d人,治愈率%.2f" % (num1, num2, rate))
