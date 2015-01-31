# -*- coding: utf-8 -*-

n, k = map(int, input().split())
piles = list(map(int, input().split()))

if max(piles) - min(piles) > k:
    print('NO')
else:
    print('YES')
    for i in range(n):
        print(' '.join([str(j % k + 1) for j in range(piles[i])]))
