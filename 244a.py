#!/usr/bin/env python
# -*- coding: utf-8 -*-
n, k = map(int, raw_input().split())
a = map(int, raw_input().split())
l = list()
bottom = 1
for i in xrange(k):
    print a[i],
    count = 0
    for j in xrange(bottom, n * k + 1):
        if j not in a:
            print j,
            count += 1
        if count == n - 1:
            print
            bottom = j + 1
            break
