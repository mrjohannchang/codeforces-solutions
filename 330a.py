#!/usr/bin/env python3
# -*- coding: utf-8 -*-


r, c = list(map(int, input().split()))
m = [input () for _ in range(r)]
print(sum(c for r in m if 'S' not in r)
        + sum((r - sum(1 for r in m if 'S' not in r))
            for c in zip(*m) if 'S' not in c))
