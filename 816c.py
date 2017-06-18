# -*- coding: utf-8 -*-

n, m = map(int, input().split())
g = list()
moves = list()
m1, m2 = 'row', 'col'

for _ in range(n):
    g.append(list(map(int, input().split())))

if n > m:
    g = list(map(list, zip(*g)))
    n, m = m, n
    m1, m2 = m2, m1

for i in range(n):
    while min(g[i]) > 0:
        for j in range(m):
            g[i][j] -= 1
        moves.append('{} {}'.format(m1, i+1))

g = list(map(list, zip(*g)))
for i in range(m):
    while min(g[i]) > 0:
        for j in range(n):
            g[i][j] -= 1
        moves.append('{} {}'.format(m2, i+1))

for c in g:
    if any(c):
        moves = None

if moves is None:
    print(-1)
else:
    print(len(moves))
    print('\n'.join(moves))
