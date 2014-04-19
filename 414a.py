# -*- coding: utf-8 -*-

import sys


n, k = list(map(int, input().split()))
ans = []

if n // 2 > k or (n < 2 and k > 0):
    print(-1)
    sys.exit()

if k == 0:
    print(1)
    sys.exit()

if n // 2 == k:
    for i in range(1, n + 1):
        ans.append(i)
else:
    ans.append(k - ((n // 2) - 1))
    ans.append(2 * (k - ((n // 2) - 1)))
    for i in range(1, n - 1):
        ans.append(i + int(2e8))

ans = map(str, ans)
print(' '.join(ans))
