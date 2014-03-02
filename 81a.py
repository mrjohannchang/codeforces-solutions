#!/usr/bin/env python
# -*- coding: utf-8 -*-
s = []
for c in raw_input():
    if len(s) < 1:
        s.append(c)
    elif c == s[-1]:
        s.pop()
    else:
        s.append(c)
print ''.join(s)
