#!/usr/bin/python
# coding: UTF-8

"""
 字符串替换
"""

str1 = "你好$$$我正在学 Python@#@#现在需要&*&*&修改字符串"
str2 = str1.replace('$$$', ' ').replace('@#@#', ' ').replace('&*&*&', ' ')
print(str2)