#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/25 15:30
# @Author   : SLNotFound
# @File     : exercise01.py

"""
在终端中输入课程阶段数,显示课程名称
效果：
输入： 输出：
 1 Python语言核心编程
 2 Python高级软件技术
 3 Web 全栈
 4 项目实战
 5 数据分析、人工智能

"""

num = input("请输入课程阶段数：")
if int(num) == 1:
    print("Python语言核心编程")
elif int(num) == 2:
    print("Python高级软件技术")
elif int(num) == 3:
    print("Web 全栈")
elif int(num) == 4:
    print("项目实战")
elif int(num) == 5:
    print("数据分析、人工智能")
