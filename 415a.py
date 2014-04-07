# -*- coding: utf-8 -*-

n, m = list(map(int, input().split()))
b_list = list(map(int, input().split()))
res = [0] * n

for b in b_list:
    for i in range(b-1, n):
        if res[i] == 0:
            res[i] = str(b)

print(' '.join(res))
