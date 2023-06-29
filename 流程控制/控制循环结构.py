#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/6/27 17:11
# @Author   : SLNotFound
# @File     : 控制循环结构.py

for i in range(0, 10):
    print("i的值是：", i)
    if i == 2:
        break

print("============")
for i in range(0, 10):
    print("i的值是：", i)
    if i == 2:
        break
    else:
        print('else块： ', i)

print("=================================")
# continue
for i in range(0, 3):
    print("i的值是：", i)
    if i == 1:
        continue
    print("continue后的输出语句")

print("==========================================")


# 使用return结束方法
def test():
    for i in range(10):
        for j in range(10):
            print("i的值是：%d, j的值是：%d" % (i, j))
            if j == 1:
                return
            print("return后输出的语句")


test()
