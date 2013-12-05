#!/usr/bin/env python
# -*- coding: utf-8 -*-
table = []
n, m, k = map(int, raw_input().split())
[table.append(raw_input().split()) for i in xrange(n)]
rs, cs = [i for i in xrange(n)], [i for i in xrange(m)]
for i in xrange(k):
    s, x, y = raw_input().split()
    x, y = int(x) - 1, int(y) - 1
    if s == "c":
        buf = cs[x]
        cs[x] = cs[y]
        cs[y] = buf
    elif s == "r":
        buf = rs[x]
        rs[x] = rs[y]
        rs[y] = buf
    else:
        print table[rs[x]][cs[y]]
