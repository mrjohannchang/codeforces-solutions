#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
n, m = map(int, raw_input().split())
t = []
for _ in xrange(n):
    r = raw_input()
    rr = []
    if '1' not in r:
        print -1
        exit()
    p, c = m - r.rfind('1'), None
    for i in xrange(m):
        if r[i] == '1':
            c = 0
            rr += [c]
            continue
        if c is not None:
            c += 1
            rr += [c]
            continue
        rr += [p]
        if p == 0:
            c = 0
        p += 1
    p, c = r.find('1') + 1, None
    for i in xrange(m - 1, -1, -1):
        if r[i] == '1':
            c = 0
            continue
        if c is not None:
            c += 1
            rr[i] = min(c, rr[i])
            continue
        rr[i] = min(p, rr[i])
        if p == 0:
            c = 0
        p += 1
    t += [rr]
mini = sys.maxint
for c in xrange(m):
    mini = min(mini, sum(r[c] for r in t))
print mini
