#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/17 21:53
# @Author   : SLNotFound
# @File     : exercise03.py
"""
在终端中输入一个四位整数，计算每位相加和。
例如：录入1234，打印1+2+3+4结果
效果：
请输入四位整数：1234
结果是：10
"""

num = input("请输入四位整数：")
result = int(num) // 1000
result += int(num) % 1000 // 100
result += int(num) % 100 // 10
result += int(num) % 10
print("结果是：" + str(result))
