#!/usr/bin/python
# -*- coding: utf-8 -*-
n=input()
p=map(int,raw_input().split())
print sum(1 for i in xrange(1,n)if max(p[:i])<p[i]or min(p[:i])>p[i])
