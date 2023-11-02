#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
 定义函数,根据总两数,计算几斤零几两.:
"""

total_liang = int(input("请输入两:"))


def cal_jin_liang(num):
    return num // 16, num % 16


jin, liang = cal_jin_liang(total_liang)
print(str(jin) + "斤零" + str(liang) + "两")
