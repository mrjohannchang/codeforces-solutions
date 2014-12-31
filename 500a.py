# -*- coding: utf-8 -*-

n, t = map(int, input().split())
a = list(map(int, input().split()))

current = 0

while current < t - 1:
    current = a[current] + current

print('YES' if current == t - 1 else 'NO')
