# -*- coding: utf-8 -*-

import sys


n, s = map(int, input().split())
sqr_r = 0
arounds = []
total = s

for _ in range(n):
    x, y, k = map(int, input().split())
    arounds.append([x ** 2 + y ** 2, k])
    total += k

if total < 10 ** 6:
    print(-1)
    sys.exit()

arounds.sort()

for i in range(n):
    if s >= 10 ** 6:
        break
    s += arounds[i][-1]
    sqr_r = arounds[i][0]

print(sqr_r ** 0.5)
