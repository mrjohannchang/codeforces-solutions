#!/usr/bin/python
# -*- coding: utf-8 -*-
n, a = input(), map(int, raw_input().split())
half = sum(a) / 2
coin, quantity = 0, 0
for i, v in enumerate(reversed(sorted(a))):
    quantity += v
    coin += 1
    if quantity > half:
        break
print coin
