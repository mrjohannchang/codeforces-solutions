#!/usr/bin/env python
# -*- coding: utf-8 -*-
n, k = map(int, raw_input().split())
a = map(int, raw_input().split())
l, r = -1, -1
if k == 1:
    print 1, 1
    exit()
b = set([])
c = set([])
for i in xrange(n):
    if l != -1:
        b.add(a[i])
    elif l == -1 and a[i] != a[0]:
        l = i
        b.add(a[0])
        b.add(a[i])
    if len(b) == k:
        r = i + 1
        break
if l != -1 and r != -1:
    for i in xrange(r - 1, l - 2, -1):
        c.add(a[i])
        if len(c) == k:
            l = i + 1
            break
    print l, r
else:
    print '-1', '-1'
