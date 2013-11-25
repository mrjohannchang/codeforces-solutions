#!/usr/bin/python
# -*- coding: utf-8 -*-

n, k = map(int, raw_input().split())
l = map(int, raw_input().split())

j = 0
for i in xrange(1, 2 * n + 1, 2):
    if l[i] > (l[i-1] + 1) and l[i] > (l[i+1] + 1):
        l[i] -= 1
        j += 1
    if j == k:
        break

print(" ".join(map(str, l)))
