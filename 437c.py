# -*- coding: utf-8 -*-

n, m = map(int, input().split())
v = list(map(int, input().split()))
graph = [set() for _ in range(n)]
strengths = list()
ans = 0

for i in range(m):
    x, y = map(int, input().split())
    graph[x-1].add(y - 1)
    graph[y-1].add(x - 1)

for i in range(n):
    strengths.append([v[i], i])

strengths = list(reversed(sorted(strengths)))

while len(strengths) > 0:
    (vi, i) = strengths.pop(0)
    ans += sum(v[j] for j in graph[i])
    for s in strengths:
        if i in graph[s[1]]:
            graph[s[1]].remove(i)

print(ans)
