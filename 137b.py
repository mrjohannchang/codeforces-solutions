#!/usr/bin/env python
# -*- coding: utf-8 -*-
n = input()
m = map(int, raw_input().split())
print sum(1 for i in xrange(1, n + 1) if i not in m)
