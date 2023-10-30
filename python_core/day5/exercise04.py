#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

str1 = "To have a government that is of people by people for people"
word_list = str1.split(" ")
new_word_list = word_list[::-1]

result = " ".join(new_word_list)
print(result)
