#!/usr/bin/env python
# -*- coding: utf-8 -*-
n, k = map(int, raw_input().split())
a = [map(int, raw_input().split()) for i in xrange(n)]
print sum(((a[i][0] - a[i-1][0])**2 + (a[i][1] - a[i-1][1])**2)**0.5 for i in xrange(1, n)) * k / 50
