# -*- coding: utf-8 -*-


n, a, b = list(map(int, input().split()))
arthurs = list(map(int, input().split()))
alexanders = list(map(int, input().split()))
ans = []

for i in range(1, n + 1):
    if i in arthurs:
        ans.append('1')
    else:
        ans.append('2')

print(' '.join(ans))
