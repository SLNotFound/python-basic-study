#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
八大行星："水星" "金星" "地球" "火星" "木星" "土星" "天王星" "海王星"
 -- 创建列表存储4个行星：“水星” "金星" "火星" "木星"
 -- 插入"地球"、追加"土星" "天王星" "海王星"
 -- 打印距离太阳最近、最远的行星(第一个和最后一个元素)
 -- 打印太阳到地球之间的行星(前两个行星)
 -- 删除"海王星",删除第四个行星
 -- 倒序打印所有行星(一行一个)
"""

planet_list = ["水星", "金星", "火星", "木星"]
print(planet_list)

planet_list.insert(2, "地球")
print(planet_list)

planet_list.append("土星")
planet_list.append("天王星")
planet_list.append("海王星")
print(planet_list)

print(planet_list[0], planet_list[-1])

print(planet_list[0:2])

planet_list.remove("海王星")
print(planet_list)

del planet_list[3]
print(planet_list)

for i in range(len(planet_list) - 1, -1, -1):
    print(planet_list[i])
