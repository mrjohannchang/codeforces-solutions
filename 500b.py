# -*- coding: utf-8 -*-

n = int(input())
p = list(map(int, input().split()))
a = [list(map(int, list(input()))) for _ in range(n)]

groups = []

for i in range(n):
    s = set()
    s.add(i)
    for j in range(n):
        if a[i][j] == 1:
            s.add(j)
    if len(s) > 1:
        groups.append(s)

i = 0
while i < len(groups):
    j = i + 1
    while j < len(groups):
        if len(groups[i] & groups[j]) == 0:
            j += 1
            continue
        groups[i] |= groups[j]
        groups.pop(j)
        j = i + 1
    i += 1

groups = [sorted(list(s)) for s in groups]

for g in groups:
    i = len(g)
    while i > 0:
        j = 0
        while j < i - 1:
            if p[g[j]] > p[g[j+1]]:
                p[g[j]], p[g[j+1]] = p[g[j+1]], p[g[j]]
            j += 1
        i -= 1

print(' '.join(map(str, p)))
