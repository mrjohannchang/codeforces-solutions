#!/usr/bin/python
# -*- coding: utf-8 -*-

n, m = map(int, raw_input().split())
l = map(int, raw_input().split())
l.sort()
k = list(l)
k.reverse()

maxi, mini = 0, 0

p = 0
for i in xrange(n):
    if p != m - 1 and k[p] < k[p+1]:
        p += 1
    elif p == m - 1 and k[p] > k[p-1]:
        pass
    else:
        p = 0
    buf = k[p]
    maxi += buf
    k[p] -= 1

p = 0
for i in xrange(n):
    if l[p] == 0:
        p += 1
    buf = l[p]
    mini += buf
    l[p] -= 1

print maxi, mini
