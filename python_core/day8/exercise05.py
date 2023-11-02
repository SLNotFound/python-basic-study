#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
 创建函数,根据课程阶段计算课程名称.
"""

number = input("请输入课程阶段数：")


def course(num):
    if num == "1":
        return "Python语言核心编程"
    elif num == "2":
        return "Python高级软件技术"
    elif num == "3":
        return "Web全栈"
    elif num == "4":
        return "项目实战"
    elif num == "5":
        return "数据分析、人工智能"


lesson = course(number)

print(lesson)
