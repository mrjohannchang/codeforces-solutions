#!/usr/bin/python
# -*- coding: utf-8 -*-

n = int(raw_input())
cur_turn = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']

if n <= 5:
    print(cur_turn[n-1])
    exit()

s = lambda x: 5 * (pow(2, x) - 1)
upper_index = next(x for x in xrange(1, n) if s(x) > n)
upper_bounder = s(upper_index)
lower_bounder = s(upper_index-1)

ratio = float((n - lower_bounder)) / (upper_bounder - lower_bounder)
if ratio >= 0.8:
    print(cur_turn[4])
elif ratio >= 0.6:
    print(cur_turn[3])
elif ratio >= 0.4:
    print(cur_turn[2])
elif ratio >= 0.2:
    print(cur_turn[1])
else:
    print(cur_turn[0])
