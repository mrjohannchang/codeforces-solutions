#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
stdin = sys.stdin.read().splitlines()
del stdin[0]
c = 0
p = 0
for v in stdin:
    o, i = map(int, v.split())
    p += i - o
    c = max(c, p)
print(str(c))
