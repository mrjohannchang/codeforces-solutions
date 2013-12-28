#!/usr/bin/env python
# -*- coding: utf-8 -*-
n = input()
s = str(n)

if n <= 99:
    print n
    exit()

count = 10 ** (len(s) - 1) - 1
print count + sum(1 for i in xrange(10 ** (len(s) - 1), n + 1) if len(set(str(i))) <= 2)
