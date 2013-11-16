#!/usr/bin/python
# -*- coding: utf-8 -*-
read = lambda: map(int, raw_input().split())
xy = [[0]*1002 for i in xrange(1002)]
m, m = read()
for i in xrange(m):
    x, y = read()
    for j in xrange(x-1, x+2):
        for k in xrange(y-1, y+2):
            xy[j][k] += 1
            if xy[j][k] is 9:
                print i+1
                exit()
print -1
