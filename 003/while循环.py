#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/6/27 16:13
# @Author   : SLNotFound
# @File     : 循环.py

count = 0
while count < 10:
    print("count: ", count)
    count += 1
print("循环结束！")

# 循环遍历列表和元组
a_tuple = ('alice', 'bob', 'cindy')
i = 0
while i < len(a_tuple):
    print(a_tuple[i])
    i += 1

src_list = [12, 32, 4, 32, 44, 32, 12, 212]
a_list = []
b_list = []
c_list = []
while len(src_list) > 0:
    ele = src_list.pop()
    if ele % 3 == 0:
        a_list.append(ele)
    elif ele % 3 == 1:
        b_list.append(ele)
    else:
        c_list.append(ele)
print("整除3的：", a_list)
print("除以3余1的：", b_list)
print("除以3余2的：", c_list)
