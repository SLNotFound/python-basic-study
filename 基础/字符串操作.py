#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/6/27 14:22
# @Author   : SLNotFound
# @File     : 字符串操作.py

# 大小写
a = 'our domain is crazyit.org'
print(a.title())
print(a.upper())
print(a.lower())

# 删除空白
s = ' this is a puppy '
# 删除左边的空格
print(s.lstrip())
# 删除右边的空格
print(s.rstrip())
# 删除两边的空格
print(s.strip())
print(s)

s2 = 'i think it is a scarecrow'
print(s2.lstrip('itow'))
print(s2.rstrip('itow'))
print(s2.strip('itow'))
