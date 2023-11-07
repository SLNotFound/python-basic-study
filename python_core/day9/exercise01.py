#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
 创建手机类，实例化两个对象并调用其函数，最后画出内存图。
数据：品牌、价格、颜色
行为：通话
"""


class MobilPhone:

    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def call(self):
        print("call")


huawei = MobilPhone("华为", 2000, "黑色")
huawei.call()
