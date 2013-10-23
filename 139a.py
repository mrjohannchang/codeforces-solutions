#!/usr/bin/env python
# -*- coding: utf-8 -*-
n, wps = input(), map(int, raw_input().split())
i, summ = 0, 0
while summ < n:
    if i == 7:
        i = 1
    else:
        i += 1
    summ += wps[i-1]
print i
