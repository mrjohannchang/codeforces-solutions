#!/usr/bin/env python
# -*- coding: utf-8 -*-
n = input()
s = []
[s.append(map(int, raw_input().split())) for i in xrange(n)]
cs = []
rs = []
[cs.append(sum(s[j][i] for j in xrange(n))) for i in xrange(n)]
[rs.append(sum(s[i][j] for j in xrange(n))) for i in xrange(n)]
print sum(1 for i in xrange(n) for j in xrange(n) if cs[i] > rs[j])
