#!/usr/bin/env python
# -*- coding: utf-8 -*-
k, l, la = input(), input(), 0
la = 0
def find_root(l, k):
    global la
    if l == k:
        return True
    if l % k != 0 or l < k * k:
        return False
    la += 1
    l /= k
    return find_root(l, k)
if find_root(l, k):
    print 'YES'
    print la
else:
    print 'NO'
