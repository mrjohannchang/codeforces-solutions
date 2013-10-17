#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
n, ts = input(), map(int, raw_input().split())
td = {}
tss = set(ts)
summ = 0
for t in tss:
    td[t] = ts.count(t)
for t in tss:
    if t == 0:
        if td[t] > 1:
            summ += td[t] * (td[t] - 1) / 2
        continue
    if 0 - t in td:
        summ += td[t] * td[0-t]
        del td[t]
        del td[0-t]
print summ
