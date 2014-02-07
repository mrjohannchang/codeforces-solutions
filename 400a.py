#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for _ in range(int(input())):
    cards = input()
    count = 0
    output = ''
    if 'X' in cards:
        count += 1
        output += ' 1x12'
    for q, p in zip(cards[:6], cards[6:]):
        if q == p == 'X':
            count += 1
            output += ' 2x6'
            break
    for q, p, r in zip(cards[:4], cards[4:8], cards[8:]):
        if q == p == r == 'X':
            count += 1
            output += ' 3x4'
            break
    for q, p, r, s in zip(cards[:3], cards[3:6], cards[6:9], cards[9:]):
        if q == p == r == s == 'X':
            count += 1
            output += ' 4x3'
            break
    for q, p, r, s, t, u in zip(cards[:2], cards[2:4], cards[4:6], cards[6:8], cards[8:10], cards[10:]):
        if q == p == r == s == t == u == 'X':
            count += 1
            output += ' 6x2'
            break
    if 'O' not in cards:
        count += 1
        output += ' 12x1'
    print(str(count) + output)
