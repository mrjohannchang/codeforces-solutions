# -*- coding: utf-8 -*-

a, b = map(int, input().split())

res = 0

while a > 0 and b > 0 and a != b:
    res += a // b
    a, b = b, a % b

print(res)
