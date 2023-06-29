#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/6/29 17:29
# @Author   : SLNotFound
# @File     : 方法.py


class Fruit:
    price = 0

    def __int__(self):
        self.__color = 'Red'
        self.__city = 'Kunming'

    def __outputColor(self):
        print(self.__color)

    def __outputCity(self):
        print(self.__city)

    def output(self):
        self.__outputColor()
        self.__outputCity()

    @staticmethod
    def getPrice():
        return Fruit.price

    @staticmethod
    def setPrice(p):
        Fruit.price = p


apple = Fruit()
apple.output()
print(Fruit.getPrice())
Fruit.setPrice(9)
print(Fruit.getPrice())

