#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
循环录入编码值打印文字，直到输入空字符串停止。
效果：
请输入数字：113
q
请输入数字：116
t
请输入数字：
Process finished with exit code 0
"""
while True:
    test_num = input("请输入数字：")
    if test_num == '':
        break
    else:
        print(chr(int(test_num)))
