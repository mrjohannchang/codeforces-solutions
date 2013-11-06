#!/usr/bin/python
# -*- coding: utf-8 -*-
count, x, y, z = 0, {}, {}, []
for i in xrange(input()):
    a, b = map(int, raw_input().split())
    if a not in x:
        x[a] = set()
    if b not in y:
        y[b] = set()
    x[a].add(b)
    y[b].add(a)
    z.append((a, b))
for a, b in z:
    if any(True for i in x[a] if i < b) and any(True for i in x[a] if i > b) \
            and any(True for i in y[b] if i < a) and any(True for i in y[b] if i > a):
        count += 1
print count
