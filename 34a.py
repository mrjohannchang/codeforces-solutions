#!/usr/bin/env python
# -*- coding: utf-8 -*-
n = input()
soldiers = map(int, raw_input().split())
# ssoldiers = sorted(soldiers)
ssoldiers = soldiers
ssoldiers.append(ssoldiers[0])
minhdiff = 1001
for i in xrange(n):
    minhdiff = min(minhdiff, abs(ssoldiers[i] - ssoldiers[i+1]))
for i in xrange(n):
    if abs(ssoldiers[i] - ssoldiers[i+1]) == minhdiff:
        # ii = soldiers.index(ssoldiers[i]) + 1
        # if minhdiff == 0:
            # print ii, soldiers[ii:].index(ssoldiers[i+1]) + 1 + ii
        # else:
            # print ii, soldiers.index(ssoldiers[i+1]) + 1
        i += 1
        print i,
        if i + 1 > n:
            print 1
        else:
            print i + 1
        break
