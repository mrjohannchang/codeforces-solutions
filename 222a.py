#!/usr/bin/env python
# -*- coding: utf-8 -*-
n, k = map(int, raw_input().split())
aseq = map(int, raw_input().split())
if len(set(aseq[k-1:])) > 1:
    print -1
    exit()
if k >= 2:
    for i in xrange(k-2, -1, -1):
        if aseq[k-1] != aseq[i]:
            print i + 1
            exit()
print 0
