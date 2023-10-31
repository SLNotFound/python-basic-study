#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""

"""

dict_travel_info = {
    "北京": {
        "景区": ["长城", "故宫"],
        "美食": ["烤鸭", "豆汁焦圈", "炸酱面"]
    },
    "四川": {
        "景区": ["九寨沟", "峨眉山"],
        "美食": ["火锅", "兔头"]
    }
}

print(dict_travel_info["北京"]["景区"][0])
print(dict_travel_info["四川"]["美食"][1])

for city in dict_travel_info:
    print(city)

for item in dict_travel_info["北京"]["美食"]:
    print(item)

for values in dict_travel_info.values():
    for item in values["美食"]:
        print(item)

