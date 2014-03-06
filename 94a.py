#!/usr/bin/python
# -*- coding: utf-8 -*-

s = raw_input()
d = {}
for i in xrange(10):
    d[raw_input()] = str(i)
ret = ""
for i in xrange(0, len(s), 10):
    ret += d[s[i:i+10]]
print(ret)
