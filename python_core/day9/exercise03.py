#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
 以面向对象思想,描述下列情景.
玩家攻击敌人,敌人受伤(头顶爆字).
"""


class Player:
    def __init__(self, player_name):
        self.name = player_name

    def attack(self, enemy):
        print(enemy + "减少血量")


xm = Player("玩家")
xm.attack("敌人")
