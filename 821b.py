# -*- coding: utf-8 -*-


m, b = map(int, input().split())
x, y = m*b, b
s = 0

for j in range(y+1):
    i = m * (b - j)
    a1 = i * (1 + i) >> 1
    d = i + 1
    n = j + 1
    s = max(s, n * (2 * a1 + (n - 1) * d) >> 1)

print(s)
