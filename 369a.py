#!/usr/bin/env python3
# -*- coding: utf-8 -*-


n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))
st = a.count(1)
nd = a.count(2)
if st > m:
    ans = st - m
    ans += max(0, nd - k)
else:
    ans = max(0, nd - (k + m - st))
print(ans)
