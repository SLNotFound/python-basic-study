#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
将两个列表，合并为一个字典
姓名列表["张无忌","赵敏","周芷若"]
房间列表[101,102,103]
{101: '张无忌', 102: '赵敏', 103: '周芷若'}
"""
name_list = ["张无忌", "赵敏", "周芷若"]
room_list = [101, 102, 103]
info_dict = {name_list[i]: room_list[i] for i in range(len(name_list))}
print(info_dict)

info_dict1 = {}
for k, v in info_dict.items():
    info_dict1[v] = k
print(info_dict1)
