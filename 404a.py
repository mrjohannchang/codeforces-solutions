#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


n = int(input())

lines = [input() for _ in range(n)]

if len(set(c for l in lines for c in l)) != 2:
    print('NO')
    sys.exit()

for i in range(n):
    if lines[0][0] != lines[i][i] or lines[0][0] != lines[i][-i-1]:
        print('NO')
        sys.exit()
    if lines[i].count(lines[0][0]) != (1 if i == n // 2 else 2):
        print('NO')
        sys.exit()
print('YES')
