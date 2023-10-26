#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/25 15:30
# @Author   : SLNotFound
# @File     : exercise01.py

"""
一张纸的厚度是0.01毫米
请计算，对折多少次超过珠穆朗玛峰(8844.43米)
思路:
数据：厚度、高度、次数
算法：厚度*=2 次数+=1
"""
count = 0
h = 0.00001
while True:
    count += 1
    h *= 2
    print("第%d次对折，厚度为%d" % (count, h))
    if h > 8844.43:
        print("总共对折了%d次" % count)
        break

