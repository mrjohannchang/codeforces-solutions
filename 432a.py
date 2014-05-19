# -*- coding: utf-8 -*-


n, k = map(int, input().split())
s = list(map(int, input().split()))
print(sum(1 for i in s if 5 - i >= k) // 3)
