# -*- coding: utf-8 -*-

n, k = map(int, input().split())
res = n

for _ in range(k):
    if res % 10:
        res -= 1
    else:
        res = int(res / 10)

print(res)
