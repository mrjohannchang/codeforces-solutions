#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n, p, k = map(int, input().split(' '))

s = '({})'.format(str(p))

for i in range(1, k + 1):
    if p - i > 0:
        s = str(p - i) + ' ' + s
    if p + i <= n:
        s += ' ' + str(p + i)

if s[0] != '(' and int(s.split(' ')[0]) > 1:
    s = '<< ' + s
if s[-1] != ')' and int(s.split(' ')[-1]) < n:
    s += ' >>'

print(s)
