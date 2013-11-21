#!/usr/bin/python
# -*- coding: utf-8 -*-

def ep(msg):
    print(str(msg))
    exit()

n = raw_input()
l = map(int, raw_input().split())

if 0 not in l:
    ep(-1)

if sum(l) == 0:
    ep(0)

l.sort()

r = sum(l) % 3
if r == 0:
    l.reverse()
    ep(''.join(map(str, l)))

i = next((i for i, v in enumerate(l) if v % 3 == r), -1)
if i != -1:
    del l[i]
else:
    del l[next(i for i, v in enumerate(l) if v % 3 == 3 - r)]
    del l[next(i for i, v in enumerate(l) if v % 3 == 3 - r)]

if sum(l) == 0:
    ep(0)

l.reverse()
ep(''.join(map(str, l)))
