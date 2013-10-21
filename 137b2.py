#!/usr/bin/env python
# -*- coding: utf-8 -*-
n = input()
a = map(int, raw_input().split())
m = [1] * (n + 1)
for i in xrange(n):
    if a[i] <= n:
        m[a[i]] = 0
print sum(m) - 1
