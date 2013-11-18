#!/usr/bin/python
# -*- coding: utf-8 -*-

n = int(raw_input())
lst = map(int, raw_input().split(' '))
print(str(sum(max(0, lst[i-1]-lst[i]) for i in xrange(1, n))))
