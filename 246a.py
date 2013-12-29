#!/usr/bin/env python
# -*- coding: utf-8 -*-
n = input()

if n < 3:
    print -1
    exit()

for i in xrange(1, n + 1):
    if i == 1:
        print 2,
    elif i == 2:
        print 3,
    elif i == 3:
        print 1,
    else:
        print i,
