#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/6/27 15:41
# @Author   : SLNotFound
# @File     : 创建列表和元组.py

my_list = ['test', 20, 'Python']
print(my_list)

my_tuple = ('test', 20, 'Python')
print(my_tuple)

# 列表和元组的通用方法
print(my_list[0])
print(my_tuple[1])
print(my_tuple[-1])
print(my_list[-2])

# in运算符
a_tuple = ('alice', 21, 'cooper')
print(21 in a_tuple)
print(11 in a_tuple)
print('alice' not in a_tuple)
