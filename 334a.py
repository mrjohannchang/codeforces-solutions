#!/usr/bin/env python3
# -*- coding: utf-8 -*-


n = int(input())
n2 = n * n
ans = list()
for i in range(1, n2 // 2 + 1):
    ans.append(str(i))
    ans.append(' ')
    ans.append(str(n2 - i + 1))
    ans.append(' ' if (i // 2) % n else '\n')
print(''.join(ans))
