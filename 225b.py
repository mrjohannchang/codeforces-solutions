#!/usr/bin/env python
# -*- coding: utf-8 -*-
kbs, ans = [0, 1], [0]
s, k = map(int, raw_input().split())
while kbs[-1] < s:
    kbs.append(sum(kbs[0-min(len(kbs),k):]))
while s > 0:
    if kbs[-1] <= s:
        ans.append(kbs.pop())
        s -= ans[-1]
    else:
        kbs.pop()
print len(ans)
print ' '.join(map(str, ans))
