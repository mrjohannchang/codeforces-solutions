# -*- coding: utf-8 -*-

import itertools


g = [list(map(int, input().split())) for _ in range(5)]
maximum = 0

for p in itertools.permutations(range(5)):
    p = list(p)
    maximum = max(maximum, g[p[0]][p[1]] + g[p[1]][p[0]] + g[p[2]][p[3]]
            + g[p[3]][p[2]] + g[p[1]][p[2]] + g[p[2]][p[1]] + g[p[3]][p[4]]
            + g[p[4]][p[3]] + g[p[2]][p[3]] + g[p[3]][p[2]] + g[p[3]][p[4]]
            + g[p[4]][p[3]])

print(maximum)
