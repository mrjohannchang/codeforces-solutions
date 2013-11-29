#!/usr/bin/env python
# -*- coding: utf-8 -*-

p, d = map(int, raw_input().split())
i = 1
while True:
    r = i * ((p + 1) / i) - 1
    if r >= p - d:
        ret = r
    else:
        break
    i *= 10
print ret

# time limit exceeded
'''
p, d = map(int, raw_input().split())
num = ''
maxi = 0
bound = p - d
pp = p
while p >= bound:
    s = str(p)
    n = len(s) - 1
    if maxi > n:
        break
    if s[n] != '9':
        p -= 1
        continue
    c = 1
    while n >= 0:
        if s[n] != '9' or n == 0:
            if s[n] == '9':
                c += 1
            if c > maxi:
                maxi = c
                num = str(s)
            break
        n -= 1
        c += 1
    p -= 1
if num == '':
    print pp
else:
    print num
'''
