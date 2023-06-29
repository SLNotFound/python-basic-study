#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/6/29 17:24
# @Author   : SLNotFound
# @File     : 私有成员和公有成员.py

class Car:
    price = 100000

    def __init__(self, c, w):
        self.color = c
        self.__weight = w


car1 = Car("Red", 10.5)
car2 = Car("Blue", 12.0)
print(car1.color)
print(car1.__Car__weight)
print(car1.__weight)
