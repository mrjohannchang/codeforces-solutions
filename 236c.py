#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fractions import gcd
n, m = input(), []
if n < 3:
    print n
    exit()
for i in xrange(2, n):
    g1 = gcd(n, n - i)
    g2 = gcd(n - 1, n - i)
    m += [n * (n - 1) * (n - i) / (g1 * g2)]
    if g1 == 1 and g2 == 1:
        break
print max(m)
