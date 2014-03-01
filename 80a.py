#!/usr/bin/env python
# -*- coding: utf-8 -*-
# def gcd(a, b):
    # if a % b == 0: return b else: return (b, a % b)
import fractions
n, m = map(int, raw_input().split())
for i in xrange(2, m):
    if fractions.gcd(m, i) != 1:
        print 'NO'
        exit()
for i in xrange(n + 1, m):
    if not any(fractions.gcd(i, j) != 1 for j in xrange(2, i)):
        print 'NO'
        exit()
print 'YES'
