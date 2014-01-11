#!/usr/bin/env python
# -*- coding: utf-8 -*-
def count_pair(n):
    res = 0
    for i in xrange(1, n):
        res += i
    return res

if __name__ == '__main__':
    n = input()
    a = map(int, raw_input().split())
    odd, even = 0, 0
    even = sum(1 for i in a if i == 1 or i % 2 == 0)
    odd = sum(1 for i in a if i != 1 and i % 2 == 1)
    print count_pair(even) + count_pair(odd)
