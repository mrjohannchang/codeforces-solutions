#!/usr/bin/python
# -*- coding: utf-8 -*-

f = lambda: map(int, raw_input().split())
n = input()
seq = f()
a, b, c, d, e = f()
counts = [0, 0, 0, 0, 0]
score = 0
for p in seq:
    score += p
    if score >= e:
        counts[4] += score / e
        score = score % e
    if score >= d:
        counts[3] += score / d
        score = score % d
    if score >= c:
        counts[2] += score / c
        score = score % c
    if score >= b:
        counts[1] += score / b
        score = score % b
    if score >= a:
        counts[0] += score / a
        score = score % a
print(' '.join(map(str, counts)))
print(str(score))
