#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/6/27 15:47
# @Author   : SLNotFound
# @File     : 列表.py

# 将元组转换为列表
a_tuple = ('alice', 21, 'cooper')
a_list = list(a_tuple)
print(a_list)

a_range = range(1, 5)
print(a_range)
b_list = list(a_range)
print(b_list)

c_list = list(range(1, 20, 3))
print(c_list)

# 将列表转换为元组
test_list = ['alice', 21, 'cooper']
test_tuple = tuple(test_list)
print(test_tuple)

# 增加列表元素
a_list.append('test')
print(a_list)

# 删除列表元素
del a_list[0]
print(a_list)
