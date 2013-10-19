#!/usr/bin/python
# -*- coding: utf-8 -*-
n, p, d = input(), map(int, raw_input().split()), {}

for i, v in enumerate(p):
    d[v] = i + 1
for i in xrange(n):
    print d[i+1],
