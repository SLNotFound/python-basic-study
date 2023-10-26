#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/25 15:30
# @Author   : SLNotFound
# @File     : exercise01.py

"""
程序产生1个,1到100之间的随机数。
让玩家重复猜测,直到猜对为止。
每次提示：大了、小了、恭喜猜对了,总共猜了多少次。
"""
import random

random_number = random.randint(1, 100)
count = 1
while True:
    number = int(input("请输入要猜的数字："))

    if random_number > number:
        print("小了")
        count += 1
    elif random_number < number:
        print("大了")
        count += 1
    else:
        print("恭喜猜对啦,总共猜了%d次." % count)
        break
