#!/usr/bin/env python3
# -*- coding: utf-8 -*-


n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
a.insert(0, 1)
print(sum([a[i] - a[i-1], n - a[i-1] + a[i]][a[i] < a[i-1]]
    for i in range(1, m + 1)))
