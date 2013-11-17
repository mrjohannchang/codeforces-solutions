#!/usr/bin/python
# -*- coding: utf-8 -*-

n, towns = input(), map(int, raw_input().split())
min_time = min(towns)
if towns.count(min_time) > 1:
    print('Still Rozdil')
else:
    print(str(towns.index(min_time) + 1))
