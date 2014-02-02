#!/usr/bin/env python
# -*- coding: utf-8 -*-
n, bars = input(), map(int, raw_input().split())
print max(bars.count(i) for i in set(bars)), len(set(bars))
