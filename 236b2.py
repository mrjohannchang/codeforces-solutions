#!/usr/bin/env python
# -*- coding: utf-8 -*-
a, b, c = map(int, raw_input().split())
m = a * b * c + 1
d = [1] * m
ans = 0
for i in xrange(2, m):
    for j in xrange(i, m, i):
        d[j] += 1
for ai in xrange(1, a + 1):
    for bi in xrange(1, b + 1):
        for ci in xrange(1, c + 1):
            ans += d[ai*bi*ci]
print ans % 1073741824
