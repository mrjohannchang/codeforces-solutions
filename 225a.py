#!/usr/bin/env python
# -*- coding: utf-8 -*-
n = input()
top = input()
top_n_down = [top, 7 - top]
for i in xrange(n):
    if any([j in top_n_down for j in map(int, raw_input().split())]):
        print 'NO'
        exit()
print 'YES'
