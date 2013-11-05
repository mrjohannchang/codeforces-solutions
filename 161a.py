#!/usr/bin/env python
# -*- coding: utf-8 -*-
I = lambda: map(int, raw_input().split())
n, m, x, y = I()
a, b = I(), I()
l = []
j = 0
for i in xrange(n):
    while j < m and b[j] <= a[i] + y:
        if a[i] - x <= b[j]:
            j += 1
            l += [(i + 1, j)]
            break
        j += 1
print len(l)
for i, j in l:
    print i, j
