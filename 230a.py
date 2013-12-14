#!/usr/bin/env python
# -*- coding: utf-8 -*-
s, n = map(int, raw_input().split())
a = [(map(int, raw_input().split())) for _ in xrange(n)]
for x, y in sorted(a):
    if s > x:
        s += y
    else:
        print 'NO'
        exit()
print 'YES'
