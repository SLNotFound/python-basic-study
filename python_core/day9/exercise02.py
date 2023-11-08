#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
 以面向对象思想,描述下列情景.
小明请保洁打扫卫生
"""


class Boss:
    def __init__(self, boss_name):
        self.name = boss_name

    def hire(self, person):
        print(self.name + "请" + person + "打扫卫生")


xm = Boss("小明")
xm.hire("保洁")
