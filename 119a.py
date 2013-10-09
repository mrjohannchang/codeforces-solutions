#!/usr/bin/python
# -*- coding: utf-8 -*-

from fractions import gcd

a, b, n = map(int, raw_input().split())

while n >= 0:
    if n > 0 and gcd(a, n) <= n:
        n -= gcd(a, n)
    else:
        print(str(1))
        break
    if n > 0 and gcd(b, n) <= n:
        n -= gcd(b, n)
    else:
        print(str(0))
        break
