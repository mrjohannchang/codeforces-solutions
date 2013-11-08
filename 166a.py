#!/usr/bin/env python
# -*- coding: utf-8 -*-
n, k = map(int, raw_input().split())
table = []
[table.append(map(int, raw_input().split())) for _ in xrange(n)]
print table.count(sorted(table, cmp=lambda x, y: cmp(x[0], y[0]) if x[0] != y[0] else -cmp(x[1], y[1]), reverse=True)[k-1])
