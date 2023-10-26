#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/25 15:30
# @Author   : SLNotFound
# @File     : exercise01.py

"""
在终端中循环录入5个成绩,
最后打印平均成绩(总成绩除以人数)
效果：
请输入成绩：98
请输入成绩：83
请输入成绩：90
请输入成绩：99
请输入成绩：78
平均分：89.6
"""
score = 0
count = 0
while count < 5:
    score += float(input("请输入成绩："))
    count += 1


print("平均分：" + str(score / 5))
