#!/usr/bin/python
# -*- coding: utf-8 -*-

l = map(int, raw_input().split(' '))
scorces = map(int, raw_input().split(' '))
print(str(sum(1 for v in scorces if v >= scorces[l[1]-1] and v > 0)))
