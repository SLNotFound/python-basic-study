#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
字符串： content = "我是京师监狱狱长金海。"
 打印第一个字符、打印最后一个字符、打印中间字符
 打印字前三个符、打印后三个字符
 命题：金海在字符串content中
 命题：京师监狱不在字符串content中
 通过切片打印“京师监狱狱长”
 通过切片打印“长狱狱监师京”
 通过切片打印“我师狱海”
 倒序打印字符
"""

content = "我是京师监狱狱长金海。"
print(content[0])
print(content[-1])
print(content[1:-1])
print("金海" in content)
print("京师监狱" not in content)
print(content[2:8])
print(content[-4:1:-1])
print(content[0::3])
print(content[::-1])
