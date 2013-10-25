#!/usr/bin/python
# -*- coding: utf-8 -*-
n = input()
line = map(int, raw_input().split())
minimum = min(line)
maximum = max(line)
count = line.index(maximum)
line.pop(count)
line.insert(0, count)
line.reverse()
count += line.index(minimum)
print count
