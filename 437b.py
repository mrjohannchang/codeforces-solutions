# -*- coding: utf-8 -*-

s, l = map(int, input().split())
d = [list() for _ in range(l)]
ans = list()

for i in range(l):
    d[i] = [int('1' + '0' * bin(i + 1)[2:][::-1].index('1'), 2), i + 1]

for v in reversed(sorted(d)):
    if v[0] <= s:
        s -= v[0]
        ans.append(str(v[1]))

if s > 0:
    print(-1)
else:
    print(len(ans))
    print(' '.join(ans))
