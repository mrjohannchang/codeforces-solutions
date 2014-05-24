# -*- coding: utf-8 -*-

n = int(input())
w = list(map(int, input().split()))

one_hundred = w.count(100)
two_hundred = w.count(200)

if one_hundred % 2 == 1 or (two_hundred % 2 == 1 and one_hundred == 0):
    print('NO')
else:
    print('YES')
