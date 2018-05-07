# -*- coding: utf-8 -*-

n = int(input())
s = input()
d = {}

for i in range(n-2, -1, -1):
    ss = s[i:i+2]
    if not d.get(ss):
        d[ss] = 0
    d[ss] += 1

print(max(d, key=lambda x: d[x]))
