#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
 创建计算治愈比例的函数
"""

confirmed = int(input("请输入确诊人数:"))
cure = int(input("请输入治愈人数:"))


def cal(num1, num2):
    return num1 / num2 * 100


cure_rate = cal(cure, confirmed)
print("治愈比例为" + str(cure_rate) + "%")
