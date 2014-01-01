#!/usr/bin/env python
# -*- coding: utf-8 -*-
with open('input.txt') as f:
    n = int(f.readline())
    c = map(int, f.readline().split())
c.sort()
with open('output.txt', 'w') as f:
    if c[0] * 2 >= c[n-1]:
        f.write('0')
    else:
        l, r = 0, 0
        half_max = (c[n-1] + 1) / 2
        twice_min = c[0] * 2
        for i in xrange(n):
            if c[i] < half_max:
                l += 1
            else:
                break
            if twice_min < c[n-1-i]:
                r += 1
            else:
                break
        f.write(str(min(l, r)))
