#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/6/27 11:53
# @Author   : SLNotFound
# @File     : 字符串.py

str1 = "Hello World!"
str2 = "Alice Cooper"
print(str1)
print(str2)

# 拼接字符串
first_name = "Alice"
last_name = "Cooper"
full_name = first_name + " " + last_name
print(full_name)

# 拼接字符串和数值
s1 = "这本书的价格是："
p = 99.8
# 直接用+号连接会报错
# print(s1 + p)
print(s1 + str(p))
print(s1 + repr(p))

# repr()函数
st = "I will win!"
print(st)
print(repr(st))

# 长字符串
s = '''"Let's go fishing", said Mary.
"OK, Let's go", said her brother.
they walked to a lake'''
print(s)
