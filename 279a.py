#!/usr/bin/env python
# -*- coding: utf-8 -*-
x, y = map(int, raw_input().split())

if (x == 0 and y == 0) or (x == 1 and y == 0):
    print 0
    exit()

upper_bound = max(abs(x), abs(y)) * 4

if x > y or (x > 0 and y > 0 and x == y):
    if x > y and abs(x) <= abs(y):
        print upper_bound
    elif x > 0 and y < 0 and abs(x) - abs(y) == 1:
        print upper_bound - 4
    else:
        print upper_bound - 3
else:
    if x < y and abs(x) <= abs(y):
        print upper_bound - 2
    else:
        print upper_bound - 1
