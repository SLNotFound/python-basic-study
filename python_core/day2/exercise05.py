#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/17 21:53
# @Author   : SLNotFound
# @File     : exercise03.py
"""
古代的秤，一斤十六两。在终端中获取两，计算几斤零几两。
效果：
    请输入总两数：100
    结果为：6斤4两
"""
weight = input("请输入总两数：")
result1 = int(weight) // 16
result2 = int(weight) % 16
print("结果为：" + str(result1) + "斤" + str(result2) + "两")
print("结果为：%s斤%s两" % (result1, result2))
