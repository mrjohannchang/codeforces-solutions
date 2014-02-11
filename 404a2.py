# -*- coding: utf-8 -*-

g=input
n=int(g())
p=[g()for _ in range(n)]
x=p[0][0]
if len(set(c for l in p for c in l))!=2:print('NO');exit()
print('YNEOS'[any(1 for i in range(n)if x!=p[i][i]or x!=p[i][-i-1]or p[i].count(x)!=(1 if i==n//2 else 2))::2])
