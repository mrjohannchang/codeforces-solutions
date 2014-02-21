#!/usr/bin/python
# -*- coding: utf-8 -*-

s = raw_input()
l = ['h', 'e', 'l', 'l', 'o']
i = -1
for c in l:
    i = s.find(c, i + 1)
    if i == -1:
        print('NO')
        exit()
print('YES')
