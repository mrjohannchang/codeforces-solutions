#!/usr/bin/env python3
# -*- coding: utf-8 -*-


a, b = map(int, input().split())
ans, c = 0, 0
while a:
    ans += 1
    a -= 1
    c += 1
    if c == b:
        c = 0
        a += 1
print(ans)
