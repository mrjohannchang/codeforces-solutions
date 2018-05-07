# -*- coding: utf-8 -*-

n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))

x = a[k-1]

if k > 0:
    if k < n and a[k] == a[k-1]:
        x = -1
else:
    if a[0] > 1:
        x = 1
    else:
        x = -1

print(x)
