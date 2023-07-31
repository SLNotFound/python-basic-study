#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/6/30 0:09
# @Author   : SLNotFound
# @File     : 继承.py

import types

class Person(object):
    def __init__(self, name='', age=20, sex='man'):
        self.setName = name
        self.setAge = age
        self.setSex = sex
        
    def setName(self, name):
        if type(name) != str:
            print('姓名必须是字符串。')
            return 
        self.__name = name
        
    def setAge(self, age):
        if type(age) != int:
            print('年龄必须是整型。')
            return 
        self.__age = age
    
    def setSex(self, sex):
        if sex != '男' and sex != '女':
            print('性别输入错误')
            return 
        self.__sex = sex
    
    def show(self):
        print('姓名：', self.__name, '年龄：', self.__age, '性别：', self.__sex)
        
        
# 定义子类
class Student(Person):
    def __init__(self, name='', age=20, sex='man', schoolyear=2016):
        super(Student, self).__init__(name, age, sex)
        self.setSchoolyear(schoolyear)

    def setSchoolyear(self, schoolyear):
        self.__schoolyear=schoolyear

    def show(self):
        Person.show(self)
        print('入学年份：', self.__schoolyear)


if __name__ == '__main__':
    zhangsan = Person('张三', 19, '男')
    zhangsan.show()
    lisi = Student('李四', 18, '男', 2015)
    lisi.show()
    lisi.setAge(20)
    lisi.show()
