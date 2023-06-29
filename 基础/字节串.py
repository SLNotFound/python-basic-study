#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/6/27 13:59
# @Author   : SLNotFound
# @File     : 字节串.py

b1 = bytes()
b2 = 'b'
b3 = b'Hello'
print(b3)
print(b3[0])
print(b3[2:4])

# 调用bytes方法将字符串转换成bytes对象
b4 = bytes('我爱Python编程', encoding='utf-8')
print(b4)

# 利用字符串的encode()方法编码成bytes，默认使用UTF-8字符集
b5 = "学习Python很有趣".encode('utf-8')
print(b5)
