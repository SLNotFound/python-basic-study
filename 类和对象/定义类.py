#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/6/29 13:46
# @Author   : SLNotFound
# @File     : 定义类.py

class Person:
    hair = 'black'

    def __init__(self, name='Alice', age=8):
        self.name = name
        self.age = age

    def say(self, content):
        print(content)


p = Person()
print(p.name, p.age)
p.name = 'bob'

