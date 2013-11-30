#!/usr/bin/env python
# -*- coding: utf-8 -*-
def f(s, i, flag):
    if s[i] == s[i+1] or s[i] == s[i-1]:
        if not flag and i < n - 2 and s[i] == s[i+2]:
            f(s, i + 1, True)
        elif s[i] >= 'C':
            s[i] = 'A'
            f(s, i, True)
        else:
            s[i] = chr(ord(s[i]) + 1)
            f(s, i, True)

n, k = map(int, raw_input().split())
s = list(raw_input())
c = 0

if n == 1:
    pass
elif k == 2:
    ss = list(s)
    c1 = 0
    c2 = 0
    for i in xrange(n):
        if s[i] != chr(ord('A') + i % 2):
            s[i] = chr(ord('A') + i % 2)
            c1 += 1
        if ss[i] != chr(ord('B') - i % 2):
            ss[i] = chr(ord('B') - i % 2)
            c2 += 1
    if c1 < c2:
        c = c1
    else:
        c = c2
        s = ss
else:
    for i in xrange(0, n - 1):
        if s[i] == s[i+1]:
            f(s, i, False)
            c += 1

print c
print "".join(s)
