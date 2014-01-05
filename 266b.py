#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n, t = map(int, input().split(' '))
queue = list(input())

for i in range(t):
    j = 1
    while j < n:
        if queue[-j] == 'G' and queue[-j-1] == 'B':
            queue[-j], queue[-j-1] = queue[-j-1], queue[-j]
            j += 2
        else:
            j += 1

print(''.join(queue))
