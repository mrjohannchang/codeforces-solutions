# -*- coding: utf-8 -*-

ans = set()

for c in input():
    if c in 'abcdefghijklmnopqrstuvwxyz':
        ans.add(c)

print(len(ans))
