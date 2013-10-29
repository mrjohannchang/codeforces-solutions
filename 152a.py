#!/usr/bin/env python
# -*- coding: utf-8 -*-
n, m = map(int, raw_input().split())
rows = []
column_max = []
for i in xrange(n):
    rows.append(list(raw_input()))
for j in xrange(m):
    column_max.append(max(rows[i][j] for i in xrange(n)))
successful_students = set([])
for i in xrange(n):
    for j in xrange(m):
        if rows[i][j] == column_max[j]:
            successful_students.add(i)
print len(successful_students)
