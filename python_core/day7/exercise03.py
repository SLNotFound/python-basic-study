#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
多个人的多个爱好
"""

dict_hobbies = {
    "于谦": ["抽烟", "喝酒", "烫头"],
    "郭德纲": ["说", "学", "逗", "唱"],
}

for item in dict_hobbies["于谦"]:
    print(item)

print(len(dict_hobbies["郭德纲"]))

for key in dict_hobbies:
    print(key)

for values in dict_hobbies.values():
    for item in values:
        print(item)