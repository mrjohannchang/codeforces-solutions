#!/usr/bin/python
# -*- coding: utf-8 -*-

n = int(raw_input())
groups = map(int, raw_input().split(' '))
ones, twos, threes, fours = map(groups.count, range(1, 5))
cars = 0
cars += fours
cars += threes
cars += twos / 2
if twos % 2 != 0:
    cars += 1
if threes < ones:
    ones -= threes
    if twos % 2 != 0:
        ones -= 2
    if ones > 0:
        cars += ones / 4
        if ones % 4 != 0:
            cars += 1
print(str(cars))
