#!/usr/bin/python
# -*- coding: utf-8 -*-

l = map(int, raw_input().split(' '))
n = l[0]
m = l[1]
a = l[2]
width = n / a
length = m / a
if n % a != 0:
    width += 1
if m % a != 0:
    length += 1
print(str(width * length))
