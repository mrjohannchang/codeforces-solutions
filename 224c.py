#!/usr/bin/env python
# -*- coding: utf-8 -*-
b = [0, 0]
a, aa, aaa = [0], [0], []
ma = 0
s = raw_input()
for i in xrange(len(s)):
    if s[i] == '(':
        b[0] += 1
    elif s[i] == ')':
        b[0] -= 1
    elif s[i] == '[':
        b[1] += 1
    elif s[i] == ']':
        b[1] -= 1

    if b[0] == 0 and b[1] == 0:
        a += [i]
    elif b[0] < 0 or b[1] <0:
        aa += [i]

if len(a) == 1:
    print 0
    exit()

for i in xrange(len(a) - 1):
    if not any(True for v in aa if a[i] < v < a[i+1]):
        aaa += [a[i]]
        aaa += [a[i+1]]

if len(aaa) == 0:
    print 0
    exit()

i = 0
while i < len(aaa):
    if i == len(aaa) - 1:
        break
    if aaa[i] == aaa[i+1]:
        del aaa[i]
        del aaa[i]
        continue
    i += 1

for i in xrange(len(aaa) - 1):
    ma = max(ma, aaa[i+1] - aaa[i])

for i in xrange(0, len(aaa), 2):
    if aaa[i+1] - aaa[i] == ma:
        print s[aaa[i]:aaa[i+1]+1].count('[')
        print s[aaa[i]:aaa[i+1]+1]
        exit()
