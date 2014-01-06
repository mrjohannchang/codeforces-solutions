#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())
hlists, alists = list(), list()
for i in range(n):
    h, a = input().split(' ')
    hlists.append(h)
    alists.append(a)
print(sum(alists.count(e) for e in hlists))
