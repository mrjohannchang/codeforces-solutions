#!/usr/bin/env python
# -*- coding: utf-8 -*-
a, b, c = map(int, raw_input().split())
d = {}
ans = 0
d[1] = 1
for ai in xrange(1, a + 1):
    for bi in xrange(1, b + 1):
        for ci in xrange(1, c + 1):
            i = ai * bi * ci
            if i not in d:
                sqi = i ** 0.5
                d[i] = sum(2 if j != sqi else 1 for j in xrange(2, int(sqi) + 1) if i % j == 0) + 2
            ans += d[i]
print ans % 1073741824
