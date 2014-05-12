# -*- coding: utf-8 -*-

n, m = map(int, input().split())
points = list(map(int, input().split()))
segments = [input().split() for _ in range(m)]
sorted_points = sorted(points)
ans = [-1] * n

for i in range(n):
    c = '0' if i % 2 else '1'
    ans[points.index(sorted_points[i])] = c

print(' '.join(ans))
