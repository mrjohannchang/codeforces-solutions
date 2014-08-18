# -*- coding: utf-8 -*-

n = int(input())
b = list(map(int, input().split(' ')))
bmin, bmax = min(b), max(b)
print(bmax - bmin, n * (n - 1) // 2 if bmin == bmax
        else b.count(bmin) * b.count(bmax))
