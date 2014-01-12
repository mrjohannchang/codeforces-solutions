#!/usr/bin/env python
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    n = input()
    a = map(int, raw_input().split())
    m = input()
    for _ in xrange(m):
        (w, h) = map(int, raw_input().split())
        prev_h = max(a[0], a[w-1])
        print prev_h
        a[0] = prev_h + h
