#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/6/29 16:00
# @Author   : SLNotFound
# @File     : practice2.py

"""
输入学生的成绩score，
根据成绩判断是否及格
"""
input_score = input("请输入学生的成绩：")
score = int(input_score)
if score >= 90:
    print("成绩优秀！")
elif 80 <= score < 90:
    print("成绩良好")
elif 70 <= score < 80:
    print("成绩中等")
elif 60 <= score < 70:
    print("成绩勉强及格")
else:
    print("不及格！")
