#!/usr/bin/env python
# -*- coding: utf-8 -*-
n, m = map(int, raw_input().split())
m = m % sum(i for i in xrange(1, n + 1))
i = 1
while True:
    m -= i
    if m == 0:
        print 0
        exit()
    elif m < 0:
        print m + i
        exit()
    i += 1
