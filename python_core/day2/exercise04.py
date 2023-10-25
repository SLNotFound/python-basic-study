#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/17 21:53
# @Author   : SLNotFound
# @File     : exercise03.py
"""
在终端中输入一个疫情确诊人数再录入一个治愈人数，打印治愈比例
格式：治愈比例为xx%
效果：
    请输入确诊人数：500
    请输入治愈人数：495
    治愈比例为99.0%
"""
number_of_confirmed_cases = input("请输入确诊人数：")
number_of_cured = input("请输入治愈人数：")
cure_ratio = int(number_of_cured) / int(number_of_confirmed_cases) * 100
print(str(cure_ratio) + "%")
