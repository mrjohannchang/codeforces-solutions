#!/usr/bin/env python
# -*- coding: utf-8 -*-
f = lambda: map(int, raw_input().split())
n = input()
d = f()
a, b = f()
print sum(d[a-1:b-1])
