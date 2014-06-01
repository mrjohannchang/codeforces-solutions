# -*- coding: utf-8 -*-


n = int(input())
a = list(map(int, input().split()))
graph = [[' '] * 1000 for _ in range(2001)]
x, y = 0, 1000

for i in range(n):
    for j in range(a[i]):
        if i % 2:
            graph[y][x] = '\\'
            if j != a[i] - 1:
                y += 1
        else:
            graph[y][x] = '/'
            if j != a[i] - 1:
                y -= 1
        x += 1

for i in range(2000, -1, -1):
    graph[i] = ''.join(graph[i][:x])
    if not len(set(graph[i]) & set(['/', '\\'])):
        graph.pop(i)

print('\n'.join(graph))
