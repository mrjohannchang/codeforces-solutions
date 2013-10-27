#!/usr/bin/python
# -*- coding: utf-8 -*-
l = [input() for i in range(4)]
m = input()
print(len(set([i for i in xrange(1, m+1) for j in l if i % j == 0])))
