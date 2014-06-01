# -*- coding: utf-8 -*-

n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = 1
load = 0

for g in a:
    load += g
    if load > m:
        ans += 1
        load = g

print(ans)
