#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/6/27 16:02
# @Author   : SLNotFound
# @File     : if.py

s_age = input("请输入你的年龄：")
age = int(s_age)
if age > 18:
    print("你已经成年了")
    if age > 20:
        print("你是青年人")
    elif 40 < age < 60:
        print("你是老年人")
    else:
        print("你是老年人")
else:
    print("你还没有成年")
