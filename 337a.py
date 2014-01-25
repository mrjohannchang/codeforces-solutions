#!/usr/bin/env python3
# -*- coding: utf-8 -*-


n, m = list(map(int, input().split()))
f = sorted(list(map(int, input().split())))
print(min(f[i+n-1] - f[i] for i in range(m - n + 1)))
