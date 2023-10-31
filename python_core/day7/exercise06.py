#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/10/26 14:36
# @Author   : SLNotFound
# @File     : exercise.py

"""
1. 打印所有商品信息,
 格式：商品编号xx,商品名称xx,商品单价xx.
2. 打印所有订单中的信息,
格式：商品编号xx,购买数量xx.
3. 打印所有订单中的商品信息,
格式：商品名称xx,商品单价:xx,数量xx
4. 查找数量最多的订单(使用自定义算法,不使用内置函数)
5. 根据购买数量对订单列表降序(大->小)排列
"""
# 商品字典
dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}
# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]

# for keys, values in dict_commodity_infos.items():
#     print("商品编号:%d,商品名称:%s,商品单价:%d." % (keys, values["name"], values["price"]))

# for item in list_orders:
#     print("商品编号: %d,购买数量:%s." % (item["cid"], item["count"]))


# for item1 in list_orders:
#     for keys, values in dict_commodity_infos.items():
#         if item1["cid"] == keys:
#             print("商品名称:%s,商品单价:%d,数量%d." % (values["name"], values["price"], item["count"]))

# max_count = list_orders[0]["count"]
# for i in range(1, len(list_orders)):
#     if max_count < list_orders[i]["count"]:
#         max_count = list_orders[i]["count"]
# print("数量最多的订单为%d单" % max_count)

for i in range(len(list_orders) - 1):
    for j in range(i + 1, len(list_orders)):
        if list_orders[i]["count"] < list_orders[j]["count"]:
            list_orders[i], list_orders[j] = list_orders[j], list_orders[i]

print(list_orders)
