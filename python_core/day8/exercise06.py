#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
 创建函数,计算IQ等级
"""

ma1 = int(input("请输入你的心里年龄："))
ca1 = int(input("请输入你的实际年龄："))


def cal_iq(ma, ca):
    iq = ma / ca * 100
    if 140 <= iq:
        return "天才"
    elif 120 <= iq:
        return "超常"
    elif 110 <= iq:
        return "聪慧"
    elif 90 <= iq:
        return "正常"
    elif 80 <= iq:
        return "迟钝"
    else:
        return "低能"


iq_level = cal_iq(ma1, ca1)
print(iq_level)
