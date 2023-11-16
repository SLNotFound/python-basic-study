#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/11/16 9:43
# @Author   : SLNotFound
# @File     : write_message.py

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("Hello World")
