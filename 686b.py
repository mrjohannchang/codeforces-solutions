# -*- coding: utf-8 -*-

import os

n = int(input())
a = list(map(int, input().split(' ')))
steps = []
for i in range(n, -1, -1):
    for j in range(i-1):
        if a[j] <= a[j+1]:
            continue
        a[j], a[j+1] = a[j+1], a[j]
        steps.append('{} {}'.format(j+1, j+2))
print(os.linesep.join(steps))
