#!/usr/bin/env python
# -*- coding: utf-8 -*-
input()
sticks = map(int, raw_input().split())
pairs = 0
for s in set(sticks):
    pairs += sticks.count(s) / 2
print pairs / 2
