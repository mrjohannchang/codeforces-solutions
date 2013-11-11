#!/usr/bin/python
# -*- coding: utf-8 -*-

x, y = map(int, raw_input().split())
xl = []
yl = []

i = 2
z = x
while i <= x / 2:
    if z % i == 0:
        xl.append(i)
        z /= i
    i += 1
if len(xl) == 0:
    xl.append(x)

i = 2
z = y
while i <= y / 2:
    if z % i == 0:
        yl.append(i)
        z /= i
    i += 1
if len(yl) == 0:
    yl.append(y)

zl = []
for e in set(xl) | set(yl):
    for i in xrange(0, max(xl.count(e), yl.count(e))):
        zl.append(e)

print(str(reduce(lambda x, y: x * y, zl)))
