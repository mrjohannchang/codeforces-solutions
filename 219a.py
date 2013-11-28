#!/usr/bin/env python
# -*- coding: utf-8 -*-
k = input()
s = list(raw_input())
res = []
for c in set(s):
    cnt = s.count(c)
    if cnt % k != 0:
        print -1
        exit()
    res.append(c*(cnt/k))
res = "".join(res)
print res*k
