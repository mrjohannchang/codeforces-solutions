# -*- coding: utf-8 -*-


I = lambda: list(map(int, input().split()))
n, k = I()
f = [I() for i in range(n)]
print(max(v[0] if v[1] <= k else v[0] - (v[1] - k) for v in f))
