#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/6/29 17:19
# @Author   : SLNotFound
# @File     : person.py


class Person:
    num = 1

    def __init__(self, str, n):
        self.name = str
        self.age = n

    def SayHello(self):
        print("Hello!")

    def PrintName(self):
        print("姓名：", self.name, "年龄：", self.age)

    def PrintNum(self):
        print(Person.num)


p1 = Person("Alice", 21)
p2 = Person("Bob", 22)
p1.PrintName()
p2.PrintName()
Person.num = 2
p1.PrintNum()
p2.PrintNum()
