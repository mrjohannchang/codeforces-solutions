#!/usr/bin/python
# -*- coding: utf-8 -*-

n = input()
xd = {}
for i in xrange(n):
    x, y = map(int, raw_input().split())
    if not x in xd:
        xd[x] = set()
    xd[x].add(y)
ss = xd.values()
i = 0
while i < len(ss):
    j = i + 1
    m = False
    while j < len(ss):
        if ss[i] & ss[j]:
            ss[i] |= ss.pop(j)
            m = True
        else:
            j += 1
    if not m:
        i += 1
print len(ss) - 1
