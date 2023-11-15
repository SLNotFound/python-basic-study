#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/11/15 17:50
# @Author   : SLNotFound
# @File     : file_reader.py

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)