#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/25 15:30
# @Author   : SLNotFound
# @File     : exercise01.py

"""
在终端中录入4个同学身高,打印最高的值.
算法：
170 160 180 165
假设第一个就是最大值
使用假设的和第二个进行比较, 发现更大的就替换假设的
使用假设的和第三个进行比较, 发现更大的就替换假设的
使用假设的和第四个进行比较, 发现更大的就替换假设的
最后，假设的就是最大的.
效果：
请输入第1个同学身高:170
请输入第2个同学身高:160
请输入第3个同学身高:180
请输入第4个同学身高:165
最高的同学:180
"""
h1 = int(input("请输入第1个同学身高："))
h2 = int(input("请输入第2个同学身高："))
h3 = int(input("请输入第3个同学身高："))
h4 = int(input("请输入第4个同学身高："))

max_value = h1

if max_value < h2:
    max_value = h2
if max_value < h3:
    max_value = h3
if max_value < h4:
    max_value = h4

print("最高的同学：" + str(max_value))
