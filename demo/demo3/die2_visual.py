#!/usr/bin/python
# coding: UTF-8

import pygal
from die import Die

die1 = Die()
die2 = Die()

results = []
for roll_num in range(100000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling two D6 100000 times."
hist.x_labels = range(2, 12)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
# hist.render_to_file('die2_visual.svg')

print(frequencies)
