# -*- coding: utf-8 -*-


n = int(input())
g = [list(map(int, input().split())) + [i] for i in range(n)]
k = int(input())
r = [(v, i) for i, v in enumerate(list(map(int, input().split())))]
b = [None] * n

sg = sorted(g, key=lambda x: x[1], reverse=True)
sr = sorted(r)
count = 0
money = 0

for v in sg:
    for w in sr:
        if w[0] < v[0]:
            continue
        b[v[2]] = w[1]
        count += 1
        money += v[1]
        sr.remove(w)
        break

print(count, money)
for i in range(n):
    if b[i] == None:
        continue
    print(i + 1, b[i] + 1)
