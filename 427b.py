# -*- coding: utf-8 -*-

n, t, c = map(int, input().split())
ps = list(map(int, input().split()))

s = [0] + [i + 1 for i in range(n) if ps[i] > t] + [n + 1]

print(sum(s[i] - s[i-1] - c for i in range(1, len(s)) if s[i] - s[i-1] > c))
