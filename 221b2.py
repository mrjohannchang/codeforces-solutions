#!/usr/bin/env python
# -*- coding: utf-8 -*-
n = input()

if len(str(n)) == 1:
    print 1
    exit()

s = set(str(n))
r = 0
summary = 0

for i in xrange(1, int(n**0.5) + 1):
    r = n / i

    if n % i == 0:
        if len(set(str(i)) & s) != 0:
            summary += 1

    if r == i:
        continue

    if n % r == 0:
        if len(set(str(r)) & s) != 0:
            summary += 1

print summary
