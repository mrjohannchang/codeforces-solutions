#!/usr/bin/env python
# -*- coding: utf-8 -*-
x = input()
s = map(int, sorted(set(str(x))))
p = 1
ma, mi = max(s), min(s)
n = len(s)
su = 1

if n == 1:
    print 1
    exit()

if mi != 0:
    l = [mi]
else:
    l = [s[1]]

while True:
    d = int(''.join(map(str, l)))

    if d > x**0.5:
        break

    if x % d == 0:
        su += 1

    for i in xrange(p - 1, -1, -1):
        if l[i] < ma:
            l[i] = next(j for j in s if j > l[i])
            break

        l[i] = mi

        if i == 0:
            p += 1
            if mi != 0:
                l = [mi] * p
            else:
                l = [s[1]]
                l.extend([mi] * (p - 1))

print su
