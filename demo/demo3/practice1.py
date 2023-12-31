#!/usr/bin/python
# coding: UTF-8

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolors='none', s=40)
plt.show()
