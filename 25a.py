#!/usr/bin/env python
# -*- coding: utf-8 -*-
n = input()
l = map(int, raw_input().split())
odd, odd_i, even, even_i = 0, 0, 0, 0
for i in xrange(n):
    if l[i] % 2 == 0:
        even += 1
        even_i = i + 1
    else:
        odd += 1
        odd_i = i + 1
    if even != 0 and odd != 0 and (even > 1 or odd > 1):
        if even > 1:
            print odd_i
        else:
            print even_i
        break
