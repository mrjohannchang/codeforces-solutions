# -*- coding: utf-8 -*-

n = int(input())
a = list(map(int, input().split()))
d = dict()

for e in a:
    c = bin(e).count('1')
    d[c] = d.get(c, 0) + 1

print(sum(v * (v - 1) // 2 for v in d.values()))
