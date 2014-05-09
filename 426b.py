# -*- coding: utf-8 -*-


n, m = map(int, input().split())
mat = [input() for _ in range(n)]
while n > 1 and n % 2 == 0:
    if mat[:n] != list(reversed(mat[:n])):
        break
    n //= 2
print(n)
